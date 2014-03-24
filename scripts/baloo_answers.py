import json

from kitsune.questions.models import Answer

def run():
    data = []
    for a in Answer.objects.all():
        data.append(a.to_baloo())

    print json.dumps(data)
