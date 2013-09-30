import time
from datetime import date, datetime, timedelta
from math import floor

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.http import require_GET

import waffle
from statsd import statsd

from kitsune.access.decorators import login_required
from kitsune.search.es_utils import F, AnalyzerS, read_index
from kitsune.sumo.decorators import json_view
from kitsune.users.models import Profile


def display_name_or_none(user):
    try:
        return user.profile.name
    except (Profile.DoesNotExist, AttributeError):
        return None


@login_required
@require_GET
@json_view
def usernames(request):
    """An API to provide auto-complete data for user names."""
    term = request.GET.get('term', '')
    query = request.GET.get('query', '')
    pre = term or query

    if not pre:
        return []
    if not request.user.is_authenticated():
        return []
    with statsd.timer('users.api.usernames.search'):
        profiles = (
            Profile.objects.filter(Q(name__istartswith=pre))
            .values_list('user_id', flat=True))
        users = (
            User.objects.filter(
                Q(username__istartswith=pre) | Q(id__in=profiles))
            .extra(select={'length': 'Length(username)'})
            .order_by('length').select_related('profile'))

        if not waffle.switch_is_active('users-dont-limit-by-login'):
            last_login = datetime.now() - timedelta(weeks=12)
            users = users.filter(last_login__gte=last_login)

        return [{'username': u.username,
                 'display_name': display_name_or_none(u)}
                for u in users[:10]]


@require_GET
@json_view
def contributions(request, user_id):
    """Contribution metrics API view."""
    today = datetime.today()
    start_date = date(today.year - 1, today.month, today.day)

    search = (AnalyzerS().es(urls=settings.ES_URLS).indexes(
        read_index('metrics')))

    histogram = search.facet_raw(
        contributions={
            'date_histogram': {'interval': 'day', 'field': 'created'},
            'facet_filter': search._process_filters(
                [F(creator_id=int(user_id)) & F(created__gte=start_date)])
        },
        kb_edits={
            'date_histogram': {'interval': 'day', 'field': 'created'},
            'facet_filter': search._process_filters(
                [F(creator_id=int(user_id)) &
                 F(created__gte=start_date) &
                 F(locale=settings.WIKI_DEFAULT_LANGUAGE) &
                 F(model='wiki_revision')])
        },
        l10n_edits={
            'date_histogram': {'interval': 'day', 'field': 'created'},
            'facet_filter': search._process_filters(
                [F(creator_id=int(user_id)) &
                 F(created__gte=start_date) &
                 ~F(locale=settings.WIKI_DEFAULT_LANGUAGE) &
                 F(model='wiki_revision')])
        },
        answers={
            'date_histogram': {'interval': 'day', 'field': 'created'},
            'facet_filter': search._process_filters(
                [F(creator_id=int(user_id)) &
                 F(created__gte=start_date) &
                 F(model='questions_answer')])
        },
        tweets={
            'date_histogram': {'interval': 'day', 'field': 'created'},
            'facet_filter': search._process_filters(
                [F(creator_id=int(user_id)) &
                 F(created__gte=start_date) &
                 F(model='customercare_reply')])
        }
    ).facet_counts()

    data = {}
    for key in histogram.keys():
        # p['time'] is number of milliseconds since the epoch. Which is
        # convenient, because that is what the front end wants.
        data[key] = dict((p['time'], p['count']) for p in histogram[key])

    return _merge_and_massage_contributions(start_date, today, data)


DAY_IN_MILLIS = 24 * 60 * 60 * 1000.0


def _merge_and_massage_contributions(start, end, data, spacing=DAY_IN_MILLIS):
    """Takes data from shape X to shape Y.

    TODO: be more specific.
    """
    merged_data = []

    start_millis = epoch_milliseconds(start)
    # Date ranges are inclusive on both ends.
    end_millis = epoch_milliseconds(end) + spacing

    # `timestamp` is a loop counter that iterates over the timestamps
    # from start to end. It can't just be `timestamp = start`, because
    # then the zeros being adding to the data might not be aligned
    # with the data already in the graph, since we aren't counting by
    # 24 hours, and the data could have a timezone offset.
    #
    # This block picks a time up to `spacing` time after `start` so
    # that it lines up with the data. If there is no data, then we use
    # `stamp = start`, because there is nothing to align with.

    # start <= timestamp < start + spacing
    days = data['contributions'].keys()
    if days:
        timestamp = days[0]
        d = floor((timestamp - start_millis) / spacing)
        timestamp -= d * spacing
    else:
        # If there no data, it doesn't matter how it aligns.
        timestamp = start_millis

    # Iterate in the range `start` to `end`, starting from
    # `timestamp`, increasing by `spacing` each time. This ensures
    # there is a data point for each day.
    while timestamp < end_millis:
        result = {'timestamp': timestamp}
        for key, histogram in data.items():
            result[key] = histogram.get(timestamp, 0)
        merged_data.append(result)
        timestamp += spacing

    return merged_data


def epoch_milliseconds(d):
    """Convert a datetime to a number of milliseconds since the epoch."""
    return time.mktime(d.timetuple()) * 1000
