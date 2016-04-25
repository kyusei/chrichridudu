from db import Equipe
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class EquipeDAO():

    def __init__(self, idEquipe, pays, classement, goalAverage, nbGagne, nbPerdu, nbNul):
        self.idEquipe = idEquipe
        self.pays = pays
        self.classement = classement
        self.goalAverage = goalAverage
        self.nbGagne = nbGagne
        self.nbPerdu = nbPerdu
        self.nbNul = nbNul


    def get_equipe(idEquipe):
    return session.query(Equipe).filter(Equipe.idEquipe == idEquipe)


    def update_equipe():
