from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import ForeignKey, Column,DateTime, Integer, String, Date, create_engine
from sqlalchemy.orm import relationship


Base = declarative_base()
engine = create_engine('sqlite:///bd.db', echo=False)


class Match(Base):
    __tablename__ = 'match'
    idMatch = Column(Integer, primary_key=True, nullable=False)
    lieu = Column(String, nullable=False)
    date = Column(Date, default=datetime.datetime.now().date())
    idEquipe1 = Column(Integer, ForeignKey('equipe.idEquipe'), nullable=False)
    idEquipe2 = Column(Integer, ForeignKey('equipe.idEquipe'), nullable=False)


    def __init__(self, idMatch, lieu, date, idEquipe1, idEquipe2):
        

        self.idMatch = idMatch
        self.lieu = lieu
        self.date = date
        self.idEquipe1 = idEquipe1
        self.idEquipe2 = idEquipe2

    def __str__(self):
        return ("Match : [ Equipe 1: {}, Equipe 2 : {}, Date : {}, Lieu: {}]".format(self.equipeDAO.getEquipe(self.idEquipe1), self.equipeDAO.getEquipe(self.idEquipe2), self.date, self.lieu))


    def __repr__(self):
        return ("Match : [ Equipe 1: {}, Equipe 2 : {}, Date : {}, Lieu: {}]".format(self.equipeDAO.getEquipe(self.idEquipe1),  self.equipeDAO.getEquipe(self.idEquipe2), self.date, self.lieu))


class Equipe(Base):
    __tablename__ = 'equipe'
    idEquipe = Column(Integer, primary_key=True, nullable=False)
    pays = Column(String, nullable=False)
    classement = Column(Integer, nullable=False)
    goalAverage = Column(Integer, nullable=True)
    nbGagne = Column(Integer, nullable=True)
    nbPerdu = Column(Integer, nullable=True)
    nbNul = Column(Integer, nullable=True)

    def __init__(self, idEquipe, pays, classement, goalAverage, nbGagne, nbPerdu, nbNul):
        self.idEquipe = idEquipe
        self.pays = pays
        self.classement = classement
        self.goalAverage = goalAverage
        self.nbGagne = nbGagne
        self.nbPerdu = nbPerdu
        self.nbNul = nbNul

    def __str__(self):
        return (
        "Equipe : [ Pays: {}, Nombre de gagnés : {}, Nombre de perdus : {}, Nombre de nuls : {}, Goal Average :{}, Classement : {}]".format(
            self.pays, self.classement, self.nbGagne, self.nbPerdu, self.nbNul))

    def __repr__(self):
        return (
            "Equipe : [ Pays: {}, Nombre de gagnés : {}, Nombre de perdus : {}, Nombre de nuls : {}, Goal Average :{}, Classement : {}]".format(
                self.pays, self.classement, self.nbGagne, self.nbPerdu, self.nbNul))

class Score(Base):
    __tablename__ = 'resultat'
    idMatch = Column(Integer, ForeignKey(Match.idMatch), primary_key=True)
    idEquipe = Column(Integer, ForeignKey(Equipe.idEquipe), primary_key=True)
    typePoint = Column(String, nullable=False)
    temps = Column(DateTime)

    def __init__(self, idMatch, idEquipe, typePoint, temps):
        self.typePoint = typePoint
        self.temps = temps



Base.metadata.create_all(engine)
