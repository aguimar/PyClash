import unittest
from PlayerStatDataLayer import PlayerStat
from PlayerStatDataLayer import dal
from sqlalchemy.orm import sessionmaker

class Test_App(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///Stats.db')
        

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
        