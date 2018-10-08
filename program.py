import requests
import json
import pandas as pd

tag = '%23VY28C0GJ'

key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkMzNlNTQ3LWViMmYtNGI5YS1hY2Y4LWMzODkxYjViNGE2NyIsImlhdCI6MTUzODYwOTA4Mywic3ViIjoiZGV2ZWxvcGVyL2M3ZDFkNzIzLTI1MDYtMDc4MS1kMmUzLWRjZmZiN2M3OGQzNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODYuMjEzLjQ3LjI0NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.oVgZrx4Nfy1rHPur-Nq0UyUCjftf1m86ERrEZScX7qObjtBpTOYMgjNHryXkQNaNlHu7aid8JLzRDPORgho1_w'

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
obj = open("json.txt", "r").read()
pyObject = json.loads(obj)

if r.status_code == 200:
    pyObject = r.json()
    data = pd.DataFrame(pyObject['cards'], columns=['count', 'name'])
elif r.status_code == 403:
    print('Permissao Negada !')
elif r.status_code == 404:
    print('Jogador nao encontrado !')
