import json

from kitsune.users.models import User

def run():
    contributors = User.objects.filter(groups__name='Registered as contributor')
    data = []
    for u in contributors:
        try:
            data.append(u.get_profile().to_baloo())
        except:
            continue

    print json.dumps(data)
