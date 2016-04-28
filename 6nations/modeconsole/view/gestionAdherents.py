from datetime import datetime
from DAO.EquipeDAO import AdherentsDAO
from service.MatchController import ServiceAdherent

class GestionAdherent():

    def __init__(self):
        self.adherentsDAO = AdherentsDAO()

    def afficherAdherents(self):
        adherents = self.adherentsDAO.findAll()
        print("")
        print("Liste des adherent : ")
        for adherent in adherents:
            print("\t{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))
        print("")

    def afficherAjoutAdherent(self):
        alive = True
        print("")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        while alive:
            try:
                dateNaissance  = datetime.strptime(input("Date de naissance (JJ/MM/AAA) : "), "%d/%m/%Y")
                alive = False
            except ValueError:
                print("Veuillez indiquer une date valide")
        print("")
        self.adherentsDAO.insert(nom, prenom, dateNaissance)


    def afficherGradeAdherents(self):
        alive = True
        while (alive):
            adherent = self.selectionAdherent()
            print("")
            if(adherent is not None):
                alive = False
                for grade in adherent.grades:
                    print("{} obtenu le {} - {}".format(grade.libelle, grade.dateObtention, adherent.nom))
            else:
                print("Licence inconnu")
            print("")

    def afficherAjoutGradeAdherents(self):

        alive = True
        while(alive):
            adherent = self.selectionAdherent()
            if (adherent is not None):
                serviceAdherent = ServiceAdherent(adherent)
                libelleGrade = input("nom du grade : ")
                serviceAdherent.ajouterGrade(libelleGrade)
                alive = False
            else:
                print("Licence inconnu ....")
            print("")

    def selectionAdherent(self):
        adherents = self.adherentsDAO.findAll()
        print("")
        print("Liste des adherents : ")
        for adherent in adherents:
            print("\t{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))

        try:
            choixLicence = int(input("Tapez son numero de licence : "))
            adherent = self.adherentsDAO.findById(choixLicence)
            print("")
        except ValueError as valError:
            adherent = None

        return adherent
