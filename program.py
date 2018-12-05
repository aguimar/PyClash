import requests
import json
import pandas as pd
from PlayerStatDataLayer import PlayerStat, PlayerStatRepository
from clashapi import ClashApiClient

import datetime

clashapi_handler = ClashApiClient()
clash_repository = PlayerStatRepository('sqlite:///StatsRoyaleAPI.db')

players = clashapi_handler.get_players_from_clan(('clans', '%232U0GY80L'))

list_players = players.to_list()
for target_list in list_players:
    api_return = clashapi_handler.get_player_info(target_list['tag'])
    playerStat = PlayerStat(name=api_return._boxed_data['name'], trophies=api_return._boxed_data['trophies'],
                        wins=api_return._boxed_data['games']['wins'], losses=api_return._boxed_data['games']['losses'], date=datetime.datetime.now())
    clash_repository.add(playerStat)

clash_repository.save()
print('DONE !!!')