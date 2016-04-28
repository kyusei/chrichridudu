from DAO.ScoreDAO import ScoreDAO
from DAO.EquipeDAO import EquipeDAO
from models import Equipe

"""
Cette classe a pour utilité la gestion d'un professeur
Il s'occupe de la communication avec les dao
"""
class EquipeController():
    """
    constructeur
    """
    def __init__(self, professeur):
        self.professeur = professeur
        self.professeurDAO = ProfesseursDAO()
        self.diplomesDAO = DiplomesDAO()
        if(self.professeur is None):
            raise AttributeError("Le service professeur à besoin d'un objet Professeur")
        elif type(professeur) is not Professeur:
            raise AttributeError("Le service professeur à besoin d'un objet Professeur")

    """
    Permet d'ajouter un diplome a  un professeur
    """
    def ajouterDiplome(self, libelleGrade):
        self.diplomesDAO.insert(libelleGrade, self.professeur.licence)