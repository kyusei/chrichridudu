from db import Match
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class MatchDAO():

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
