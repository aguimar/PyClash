import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class PlayerStat(Base):
    
    connection = None
    engine = None
    conn_string = None
    
    __tablename__ = 'playerstats'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    trophies = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    date = Column(DateTime)

    def __repr__(self):
        return "'%s' '%s' '%s'" % (self.name, self.wins, self.losses)

    def db_init(self, conn_string):
        self.engine = create_engine(conn_string or self.conn_string)
        Base.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

dal = PlayerStat()

