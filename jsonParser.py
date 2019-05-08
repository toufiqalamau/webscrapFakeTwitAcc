import json
import ast
with open('twitterData.txt') as json_data:
    data = json.load(json_data)
    for i in data:
        if 'obama' in i['tweet'].lower():
            print(i['tweet'], i['date'])
