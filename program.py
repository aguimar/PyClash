import requests
import json
import pandas as pd
from PlayerStatDataLayer import PlayerStat, dal
from clashapi import ClashApiClient
from sqlalchemy.orm import sessionmaker
import datetime

dal.db_init('sqlite:///Stats.db')
clashapi_handler = ClashApiClient()

parameters = ('players', '%23VY28C0GJ')
api_return = clashapi_handler.get_player_json(parameters)

Session = sessionmaker(bind=dal.engine)
session = Session()
playerStat = PlayerStat(name = api_return['name'], trophies = api_return['trophies'], 
                                wins = api_return['wins'], losses = api_return['losses'], date = datetime.datetime.now())
session.add(playerStat)
session.commit()
