import json

from kitsune.kbforums.models import Post

def run():
    data = []
    for p in Post.objects.all():
        try:
            data.append(p.to_baloo())
        except:
            continue

    print json.dumps(data)
