import json

from kitsune.forums.models import Post

def run():
    data = []
    for p in Post.objects.all():
        data.append(p.to_baloo())

    print json.dumps(data)
