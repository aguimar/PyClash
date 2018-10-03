import requests
import json
import pandas as pd

tag = '%23VY28C0GJ'

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEyOWUzZGQyLTY3MzEtNDk2YS1hOGU1LWU2ZDRmMTFkNjc4OCIsImlhdCI6MTUzODMxNTc2NSwic3ViIjoiZGV2ZWxvcGVyL2M3ZDFkNzIzLTI1MDYtMDc4MS1kMmUzLWRjZmZiN2M3OGQzNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuMTkuNzIuMTY1Il0sInR5cGUiOiJjbGllbnQifV19.SFKn96tgKrGI2iKuV1F7uBhYeFgYrhlJdJPs6UDWVxhT4WpqC4uJPRVA2pLbJVUqKCnFWE3L0vr3zx3lmb83HA'

base_url = 'https://api.clashroyale.com/v1/'

clans_endpoint = base_url + 'clans/'

players_endpoint = base_url + 'players/'

tournaments_endpoint = base_url + 'tournaments/'

cards_endpoint = base_url + 'cards/'

locations_endpoint = base_url + 'locations'

headers = {
    "Accept":"Aplication/json",
    "authorization": "Bearer " + key,
}

r = requests.get(players_endpoint + tag, headers = headers)

# ler temporariamente do arquivo
    #obj = open("json.txt", "r").read()
    #pyObject = json.loads(obj)

pyObject = r.json()

data = pd.DataFrame(pyObject['cards'], columns=['count', 'name'])

if r.status_code == 200:
    #for k,v in pyObject.items():
    #    print("-->" + k,v)
    print(data)
elif r.status_code == 404:
    print('Player not found')











