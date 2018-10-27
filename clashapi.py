import collections
import requests
import json
import os

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
        
        self._key = os.getenv('MY_TOKEN', 'Token Not Found')
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
        
        if r.status_code != 200:
            raise NotImplementedError
        # TODO inspect r.status_code before return
        return r

    def get_player_json(self, endpoint, tag):
        response = self.get_player_info(endpoint,tag)
        return response.json()

    def get_players_from_clan(self, endpoint, tag):
        Endpoint = self.clashapi[endpoint]
        response = requests.get(Endpoint.url + tag + '/members', headers = self._headers)
        lista = response.json()
        return lista['items']

