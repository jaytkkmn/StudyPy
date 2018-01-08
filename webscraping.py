import json

open_file = open('AQI.json', 'r', encoding = 'utf-8')
tmp_files = open_file .read()
input_data = json. loads(tmp_files)
open_file .close()

for data in input_data:
    if '基隆市' in data['County']:
        print(data['AQI'])


