from datetime import datetime
from DAO.ProfesseursDAO import ProfesseursDAO
from service.EquipeController import ServiceProfesseur


class GestionProfesseurs():
    def __init__(self):
        self.professeursDAO = ProfesseursDAO()

    def afficherProfesseurs(self):
        professeurs = self.professeursDAO.findAll()
        print("")
        for professeur in professeurs:
            print("{} : {} {}".format(professeur.licence, professeur.prenom, professeur.nom))
        print("")

    def afficherAjoutProfesseur(self):
        print("")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        dateNaissance = datetime.strptime(input("Date de naissance (JJ/MM/AAA) : "), "%d/%m/%Y")
        print("")
        self.professeursDAO.insert(nom, prenom, dateNaissance)

    def afficherAjoutDiplome(self):
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
