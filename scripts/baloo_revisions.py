import json

from kitsune.wiki.models import Revision

def run():
    data = []
    for r in Revision.objects.all():
        data.append(r.to_baloo())

    print json.dumps(data)
