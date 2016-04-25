from matchDAO import MatchDAO
from equipeDAO import EquipeDAO
from db import *  

"""
Cette classe a pour utilité de gerer un match.
Il s'occupe de la communication avec les dao
"""
class ServiceMatch():
    """
    constructeur
    """
    def __init__(self, idEquipe1, idEquipe2, idMatch, lieu, date):
        self.idEquipe1 = idEquipe1
        self.idEquipe2 = idEquipe2
        self.idMatch = idMatch()
        self.lieu = lieu()
        self.date = date()
        
    """
    s'occupe de l'ajout des scores pour un match
    """
    def ajouterScore(self, idEquipe,idMatch, typePoint, temps):
        self.Resultat.add_score(idMatch, idEquipe, typePoint, temps)

    def ajouterMatch(self, idEquipe1, idEquipe2, lieu, date):
        self.MatchDAO.add_match(idEquipe1, idEquipe2, lieu, date)


    
