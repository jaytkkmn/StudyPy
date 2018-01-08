import requests, json

r = requests.get('http://opendata2.epa.gov.tw/AQI.json')

input_data = r.json()

for data in input_data:
    if '新店' in data['SiteName']:
        print(data['AQI'])




