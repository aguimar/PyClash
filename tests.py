import unittest
from PlayerStatDataLayer import PlayerStat, PlayerStatRepository
from PlayerStatDataLayer import dal
from sqlalchemy.orm import sessionmaker
from clashapi import ClashApi, ClashApiClient
import requests
import json
from unittest.mock import MagicMock

import pickle


class Test_App(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///StatsTests.db')
        

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
        dal.db_init('sqlite:///StatsTests.db')
        repo =  PlayerStatRepository()
        
        playerStat = PlayerStat(name = 'Aguimar', trophies = 2, wins = 1, losses = 1)
        playerStat2 = PlayerStat(name = 'Aguimar2', trophies = 2, wins = 1, losses = 1)
        repo.add(playerStat)
        repo.add(playerStat2)
        repo.save()

        # Act
        playerStatAtBD = repo.find('Aguimar2')
        
        # Assert
        self.assertEqual(playerStatAtBD, playerStat2)
    
    def test_clashapi_mock_returned_json(self):
        
        # Arrange
        binary_file = open('response_pickled.bin', 'rb')
        response_unpickled = pickle.load(binary_file)
        
        clashapi_handler = ClashApiClient()

        # uma vez mocked, posso fazer o resto sem precisa chamar a api
        clashapi_handler.get_player_info  = MagicMock(return_value = response_unpickled)

        # Act
        returned_json = clashapi_handler.get_player_json(('players', '#VY28C0GJ'))

        # Assert
        self.assertEqual(response_unpickled.json(), returned_json)
    
    def test_clashapi_integration(self):

        #clashapi_handler = ClashApiClient()

        #response = clashapi_handler.get_player_info(('players', '%23VY28C0GJ'))

        #binary_file = open('response_pickled.bin', mode='wb')
        #response_pickled = pickle.dump(response, binary_file)
        #binary_file.close()

        binary_file = open('response_pickled.bin', 'rb')
        response_unpickled = pickle.load(binary_file)

        print(response_unpickled)


        