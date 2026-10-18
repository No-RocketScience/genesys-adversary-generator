#!/usr/bin/env python3
import json

from jinja2 import Environment, FileSystemLoader

env = Environment(autoescape=True, loader=FileSystemLoader('./templates/'))

template = env.get_template("adver.html")
with open("data.json", encoding='utf-8') as f:
    data = json.load(f)

data['caracteristics'].sort(key=lambda c: c['name'])
data['skills'].sort(key=lambda c: c['name'])
data['talents'].sort(key=lambda c: c['talent'])
data['abilities'].sort(key=lambda c: c['ability'])
data['equipment'].sort(key=lambda c: c['name'])
data['defense'].sort(key=lambda c: c['name'])
data_json = json.dumps(data, separators=(',', ':')).replace("'", "\\'").replace('\\"', '\\\\"').replace('\\n', '\\\\n')# correct escaping of quotations

with open("adversary.html", 'w', encoding='utf-8') as f:
    f.write(template.render(data=data_json, **data))

