import json

data = []
with open('hw.json') as f:
    data.append(json.loads(f.read()))

data = data[0]
#load models
from allauthdemo.demo.models import Problem

for raw_data in data:
    prob = Problem(link=raw_data['link'], name=raw_data['name'], score=raw_data['score'])
    #assuming links are unique
    objs = Problem.objects.filter(link=prob.link)
    if len(objs) == 0:
        prob.save()

