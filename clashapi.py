import collections
import requests
import json

Endpoint = collections.namedtuple('Endpoint', ['endpoint', 'url'])

class ClashApi:
    
    base_url = 'https://api.clashroyale.com/v1/'
    endpoints = 'clans players tournaments cards locations'.split()

    def __init__(self):
        self._endpoints = [Endpoint(endpoint, self.base_url + endpoint + '/') for endpoint in self.endpoints]

    def __len__(self):
        return len(self._endpoints)

    def __getitem__(self, endpoint):
        return self._endpoints[self.endpoints.index(endpoint)]
    #    return self._endpoints[position]

    def getEndPoint(self, endpoint):
        return self._endpoints[self.endpoints.index(endpoint)]

class ClashApiClient:
    clashapi = ClashApi()

    def __init__(self):
        
        # TODO _tag must be parameter
        self._tag = '%23VY28C0GJ'
        
        self._key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg1MmNmMDQ1LTcxYjMtNDkyYy1iN2NmLTY0NDI5NDRlZTg0OSIsImlhdCI6MTU0MDMzNjgzNywic3ViIjoiZGV2ZWxvcGVyL2M3ZDFkNzIzLTI1MDYtMDc4MS1kMmUzLWRjZmZiN2M3OGQzNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuMjA3LjExLjE1MCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.PX6f1Gz8G6XjJRECvKL-lHUjfUT2LLU5IsqHMphwl_JVb4zVvVALPck_FcSHpIs1HqjfQXaKFnqyXQ_ttgqIKw'
        self._base_url = self.clashapi.base_url
        self._headers = {
                    "Accept":"Aplication/json",
                    "authorization": "Bearer " + self._key,
                }

    # TODO _tag must be parameter    
    def get_player_info(self, endpoint, tag):
        # TODO urllib.parse.quote(tag)
        Endpoint = self.clashapi[endpoint]
        r = requests.get(Endpoint.url + tag, headers = self._headers)
        # TODO inspect r.status_code before return
        return r

    def get_player_json(self, endpoint, tag):
        response = self.get_player_info(endpoint,tag)
        return response.json()

    def get_players_from_clan(self, parameters):
        endpoint = self.clashapi[parameters[0]]
        tag = parameters[1]
        response = requests.get(endpoint.url + tag + '/members', headers = self._headers)
        return response.json()

