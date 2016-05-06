from DAO.EquipeDAO import EquipeDAO
from DAO.MatchDAO import MatchDAO
from DAO.ScoreDAO import ScoreDAO
from models import Match

"""
Cette classe a pour utilité de gerer un adherent.
Il s'occupe de la communication avec les dao
"""
class MatchController():
    """
    constructeur
    """
    def __init__(self, match):
        self.match = match
        self.matchdao = MatchDAO()
        if self.match is None:
            raise AttributeError("error no match object")
        elif type(match) is not Match:
            raise AttributeError("error no match object")


    """
    s'occupe de l'ajout des grades pour un Adherent
    Args : libelleGrade - String
    """
    def addMatch(self,  lieu, date, id_equipe1, id_equipe2):
        self.matchdao.addMatch( lieu, date, id_equipe1, id_equipe2)


