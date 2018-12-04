import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

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


class ClanStat(Base):

    __tablename__ = 'clanstats'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class PlayerStatRepository:

    connection = None
    engine = None
    conn_string = None
    session = None

    def __init__(self, conn_string):
        self.engine = create_engine(conn_string or self.conn_string)
        Base.metadata.create_all(self.engine)
        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add(self, PlayerStat):
        self.session.add(PlayerStat)

    def find(self, key):
        return self.session.query(PlayerStat).filter_by(name=key).first()

    def save(self):
        self.session.commit()
