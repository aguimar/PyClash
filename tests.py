import unittest
from PlayerStatDataLayer import PlayerStat
from PlayerStatDataLayer import dal
from sqlalchemy.orm import sessionmaker
from clashapi import ClashApi, ClashApiHandler
import requests
import json
from unittest.mock import MagicMock


class Test_App(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///Stats.db')
        

    def test_clashapi_endpoints(self):
        # Arrange
        clashapi = ClashApi()

        # Act
        api = 'players'
        
        # Pythonic way
        endpoint2 = clashapi[api]
        
        # OO way
        endpoint = clashapi.getEndPoint(api)

        # Assert
        self.assertEquals(endpoint, endpoint2)
    
    def test_playerstat_inserted(self):
        
        # Arrange
        Session = sessionmaker(bind=dal.engine)
        session = Session()
        playerStat = PlayerStat(name = 'Aguimar', trophies = 2, wins = 1, losses = 1)
        playerStat2 = PlayerStat(name = 'Aguimar2', trophies = 2, wins = 1, losses = 1)
        session.add(playerStat)
        session.add(playerStat2)
        session.commit()

        # Act
        playerStatAtBD = session.query(PlayerStat).filter_by(name = 'Aguimar2').first()
        
        # Assert
        self.assertEqual(playerStatAtBD, playerStat)
    
    def test_clashapi_mock_returned_json(self):
        # Arrange
        
        obj = open("json.txt", "r").read()
        pyObject = json.loads(obj)
        
        clashapi_handler = ClashApiHandler()

        # uma vez mocked, posso fazer o resto sem precisa chamar a api
        clashapi_handler.clashapi_getjson = MagicMock(return_value = pyObject)

        # Act
        returned_json = clashapi_handler.clashapi_getjson('players')

        # Assert
        self.assertEqual(pyObject, returned_json)
        