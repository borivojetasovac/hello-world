#!/usr/bin/python3
import json, requests, sys

stringOfJsonData = '{"name": "Zopohie", "isCat": true, "miceCought": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

againToJson = json.dumps(jsonDataAsPythonValue)
print(againToJson)

# Fetching Current Weather Data Project
if len(sys.argv) < 2:
    print('You have to provide a location!')
    sys.exit()

location = ' '.join(sys.argv[1:])
print(location)

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

response = requests.get(url)
response.raise_for_status()

data = json.loads(response.text)
