import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('sqlite:///Stats.db', echo = True)

Base = declarative_base()

class PlayerStat(Base):
    __tablename__ = 'playerstats'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    trophies = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    date = Column(DateTime)

    def __repr__(self):
        return "'%s' '%s' '%s'" % (self.name, self.wins, self.losses)

Base.metadata.create_all(engine)
