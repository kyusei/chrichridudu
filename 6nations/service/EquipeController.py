from DAO.ScoreDAO import ScoreDAO
from DAO.EquipeDAO import EquipeDAO
from models import Equipe


class EquipeController():
    """
    constructeur
    """
    def __init__(self, professeur):
        self.equipe = Equipe
        self.equipeDAO = EquipeDAO()
        if(self.equipe is None):
            raise AttributeError("error no equipe object")
        elif type(equipe) is not Equipe:
            raise AttributeError("error no equipe object")

    """
    ajoute une equipe
    """
    def addEquipe(self, pays, classement, goalAverage, nbGagne, nbPerdu, nbNul):
        self.equipeDAO.addEquipe( pays, classement, goalAverage, nbGagne, nbPerdu, nbNul)