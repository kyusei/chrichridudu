from datetime import datetime
from DAO.EquipeDAO import EquipeDAO
from DAO.ScoreDAO import ScoreDAO
from service.EquipeController import Equipe


class GestionEquipe():
    def __init__(self):
        self.equipeDAO = EquipeDAO()

    def afficherEquipe(self):
        TEquipe = self.equipeDAO.getAllEquipe()
        print("")
        for equipe in TEquipe:
            print("{} : {} {}".format(equipe.pays, equipe.classement, equipe.goalAverage, equipe.nbGagne, equipe.nbNul, equipe.nbPerdu))
        print("")

    def afficherAjoutScore(self):
        professeur = self.selectionProfesseur()
        if (professeur is not None):
            serviceProfesseur = ServiceProfesseur(professeur)
            libelleGrade = input("nom du diplome : ")
            serviceProfesseur.ajouterDiplome(libelleGrade)
        print("")

    def afficherDiplome(self):

        professeur = self.selectionProfesseur()
        if (professeur is not None):
            for diplome in professeur.diplomes:
                print("{} obtenu le {}".format(diplome.libelle, diplome.dateObtention))
        print("")

    def selectionProfesseur(self):
        professeurs = self.professeursDAO.findAll()
        print("")
        print("Liste des professeurs")
        for professeur in professeurs:
            print("\t{} : {} {} ".format(professeur.licence, professeur.prenom, professeur.nom))
        choixLicence = int(input("Tapez son numero de licence : "))
        professeur = self.professeursDAO.findById(choixLicence)
        print("")
        return professeur
