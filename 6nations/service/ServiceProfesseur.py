from kendoDAO.DiplomesDAO import DiplomesDAO
from kendoDAO.ProfesseursDAO import ProfesseursDAO
from models import Professeur

"""
Cette classe a pour utilité la gestion d'un professeur
Il s'occupe de la communication avec les dao
"""
class ServiceProfesseur():
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