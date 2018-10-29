import collections
import requests
import json
import os
import clashroyale

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
        self._client = clashroyale.RoyaleAPI(self._key)

    # TODO _tag must be parameter    
    def get_player_info(self, tag):
        # TODO urllib.parse.quote(tag)
        r = self._client.get_player(tag)
        
        if r.response.status_code != 200:
            raise NotImplementedError
        # TODO inspect r.status_code before return
        return r

    #def get_player_json(self, endpoint, tag):
        #response = self.get_player_info(endpoint,tag)
        #return response.json()

    def get_players_from_clan(self, parameters):
        #endpoint = self.clashapi[parameters[0]]
        #tag = parameters[1]
        #response = requests.get(endpoint.url + tag + '/members', headers = self._headers)
        #list = response.json()['items']
        return list

