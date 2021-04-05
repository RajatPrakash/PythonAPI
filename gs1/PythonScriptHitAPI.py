import requests

URL = "http://127.0.0.1:8000/stuinfo/"

for i in range(4):
  if i == 0:
    i = ''
  res = requests.get(URL+str(i))
  print(res.json())
  print('\n')