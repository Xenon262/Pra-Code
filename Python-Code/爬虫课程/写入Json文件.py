import json

from sqlalchemy import false

data = [{'Name':'Ming','Sex':'Male','Birthday':'2016-6-6'},
        {'Name':'Hong','Sex':'Female','Birthday':'2000-1-1'}]
json_data = json.dumps(data,indent=2,ensure_ascii=false)

print(json_data)

with open('data.json','w',encoding='utf-8') as file:
    file.write(json_data)