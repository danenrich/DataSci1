import sys
import json



data = []
with open('output.txt') as f:
    for x in f:
        data.append(json.loads(x))
f.close