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

class ClashApiHandler:
    clashapi = ClashApi()

    def __init__(self):
        
        # TODO _tag must be parameter
        self._tag = '%23VY28C0GJ'
        
        self._key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkMzNlNTQ3LWViMmYtNGI5YS1hY2Y4LWMzODkxYjViNGE2NyIsImlhdCI6MTUzODYwOTA4Mywic3ViIjoiZGV2ZWxvcGVyL2M3ZDFkNzIzLTI1MDYtMDc4MS1kMmUzLWRjZmZiN2M3OGQzNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxODYuMjEzLjQ3LjI0NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.oVgZrx4Nfy1rHPur-Nq0UyUCjftf1m86ERrEZScX7qObjtBpTOYMgjNHryXkQNaNlHu7aid8JLzRDPORgho1_w'
        self._base_url = self.clashapi.base_url
        self._headers = {
                    "Accept":"Aplication/json",
                    "authorization": "Bearer " + self._key,
                }

    # TODO _tag must be parameter    
    def clashapi_getjson(self, parameter):
        endpoint = self.clashapi[parameter]
        r = requests.get(endpoint.url + self._tag, headers = self._headers)
        # TODO inspect r.status_code before return
        return r.json()
