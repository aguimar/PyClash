import unittest
from PlayerStatDataLayer import PlayerStat, PlayerStatRepository
from sqlalchemy.orm import sessionmaker
from clashapi import ClashApi, ClashApiClient
import requests
import json
from unittest.mock import MagicMock
from urllib.parse import quote
import datetime

import pickle


class Test_App(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        repo = PlayerStatRepository('sqlite:///StatsTests.db')

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
        self.assertEqual(endpoint, endpoint2)

    def test_playerstat_inserted(self):

        repo = PlayerStatRepository('sqlite:///StatsTests.db')
        # Arrange
        playerStat = PlayerStat(name='Aguimar', trophies=2, wins=1, losses=1)
        playerStat2 = PlayerStat(name='Aguimar2', trophies=2, wins=1, losses=1)
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
        clashapi_handler.get_player_info = MagicMock(
            return_value=response_unpickled)

        # Act
        returned_json = clashapi_handler.get_player_json(
            'players', '#VY28C0GJ')

        # Assert
        self.assertEqual(response_unpickled.json(), returned_json)

    def test_clashapi_integration(self):

        #clashapi_handler = ClashApiClient()

        #response = clashapi_handler.get_player_info(('players', '%23VY28C0GJ'))

        #binary_file = open('response_pickled.bin', mode='wb')
        #response_pickled = pickle.dump(response, binary_file)
        # binary_file.close()

        binary_file = open('response_pickled.bin', 'rb')
        response_unpickled = pickle.load(binary_file)

        print(response_unpickled)

    def test_clashapi_get_clan_members(self):

        # Arrange
        clashapi_handler = ClashApiClient()
        clash_repository = PlayerStatRepository('sqlite:///StatsFeature.db')

        # Act
        list_players = clashapi_handler.get_players_from_clan(
            'clans', '%232U0GY80L')

        for player_tag in list_players:
            api_return = clashapi_handler.get_player_json(
                'players', quote(player_tag['tag']))
            playerStat = PlayerStat(name=api_return['name'], trophies=api_return['trophies'],
                                    wins=api_return['wins'], losses=api_return['losses'], date=datetime.datetime.now())

            clash_repository.add(playerStat)

        clash_repository.save()
        # Assert

        self.assertEqual(len(playerStat), len(list_players))
