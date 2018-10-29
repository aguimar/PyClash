import requests
import json
import pandas as pd
from PlayerStatDataLayer import PlayerStat, PlayerStatRepository
from clashapi import ClashApiClient

import datetime

clashapi_handler = ClashApiClient()
clash_repository = PlayerStatRepository('sqlite:///Stats.db')

api_return = clashapi_handler.get_player_json('players', '%23VY28C0GJ')

playerStat = PlayerStat(name = api_return['name'], trophies = api_return['trophies'], 
                                wins = api_return['wins'], losses = api_return['losses'], date = datetime.datetime.now())

clash_repository.add(playerStat)
clash_repository.save()
