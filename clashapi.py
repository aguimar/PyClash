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
        
        self._key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImIzY2QyZTdlLTE1MzEtNGU1YS1hNDQ0LTg4YTcwM2Q3YjAwMCIsImlhdCI6MTUzOTMwMTQwMywic3ViIjoiZGV2ZWxvcGVyL2M3ZDFkNzIzLTI1MDYtMDc4MS1kMmUzLWRjZmZiN2M3OGQzNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODYuMjEzLjYxLjEwMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.VQ2eIj8HlqwJEi0okS_Vx3mCkm8RN-r5rZ0WlEllLTNYebqbe8lx2KDn-OxlO1DITaLYWwgR2fezRK0BcJi_jA'
        self._base_url = self.clashapi.base_url
        self._headers = {
                    "Accept":"Aplication/json",
                    "authorization": "Bearer " + self._key,
                }

    # TODO _tag must be parameter    
    def get_player_info(self, parameters):
        # TODO urllib.parse.quote(tag)
        endpoint = self.clashapi[parameters[0]]
        tag = parameters[1]
        r = requests.get(endpoint.url + tag, headers = self._headers)
        # TODO inspect r.status_code before return
        return r

    def get_player_json(self, parameters):
        return self.get_player_info(parameters).json()
