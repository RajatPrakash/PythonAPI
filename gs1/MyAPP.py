import requests


URL = "http://127.0.0.1:8000/stuDetails/"

for i in range(4):
  if i == 0:
    i = ' '
  else:
    pass
  response = requests.get(URL+str(i))
  print(response.json())