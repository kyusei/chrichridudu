from datetime import datetime

from sqlalchemy import create_engine, Table, Column, Float, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()


#Base.metadata.bind=engine
#DBSession = Sessionmaker(bind=engine)
#session=DBSession()

class Match(Base):
    __tablename__ = 'match'
    idMatch = Column(Integer, primary_key=True, nullable=False)
    lieu = Column(String, nullable=False)
    date = Column(Date, default=datetime.now().date())
    idEquipe1 = Column(Integer, ForeignKey(Equipe.idEquipe), nullable=False)
    idEquipe2 = Column(Integer, ForeignKey(Equipe.idEquipe), nullable=False)


    def __init__(self, idMatch, lieu, date):
        self.idMatch = idMatch
        self.lieu = lieu
        self.date = date


    def get_match(idMatch='', idEquipe1='', idEquipe2=''):

        result = '';
        if (idMatch != ''):
        result = session.query(Match).filter(Match.idMatch == idMatch)
        if (idMatch == '' and (idEquipe1 != '' and idEquipe2 != '')):
        result = session.query(Match).filter(Match.idEquipe1 == idEquipe1 and Match.idEquipe2 == idEquipe2)

    
        return result

    def add_match():
        match = new Match()
        session.add(Match)
        session.commit


    

class Equipe(Base):
    __tablename__ = 'equipe'
    idEquipe = Column(Integer, primary_key=True, nullable=False)
    pays = Column(String, nullable=False)
    classement = Column(Integer, nullable=False)
    goalAverage = Column(Integer, nullable=True)
    nbGagne = Column(Integer, nullable=True) 
    nbPerdu = Column(Integer, nullable=True)
    nbNul = Column(Integer, nullable=True)
    idMatch = Column(Integer, ForeignKey(Match.idMatch), nullable=False)

    def equipe_match():
        equipe = new Equipe()
        session.add(Equipe)
        session.commit

    def get_equipe(idEquipe):
    return session.query(Equipe).filter(Equipe.idEquipe == idEquipe)

    

    

class Score(Base):
    __tablename__ = 'resultat'
    idMatch = Column(Integer, ForeignKey(Match.idMatch), primary_key=True)
    idEquipe = Column(Integer, ForeignKey(Equipe.idEquipe), primary_key=True)
    typePoint = Column(String, nullable=False)
    temps = Column(Float)

    def __init__(self, typeMatch, temps):
        self.typePoint = typePoint
        self.temps = temps


    def add_score():
        score = Score()
        session.add(score)
        session.commit

        
    def get_score_by_match(idMatch):


        
Base.metadata.create_all(engine)
