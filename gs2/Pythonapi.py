import requests
import json
URL = "http://127.0.0.1:8000/studentcreate/"
data = {
  'name':'Rashika',
  'roll':1,
  'city':'delhi'

}

# print(json.dumps(data))
jdata = json.dumps(data)
r = requests.post(url=URL,data=jdata)
data =r.json() 
print(data)