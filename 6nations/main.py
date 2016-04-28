# -*-coding:UTF-8 -*
from datetime import datetime

from modeconsole.view.gestionProfesseurs import GestionProfesseurs

from DAO.EquipeDAO import AdherentsDAO
from DAO.ProfesseursDAO import ProfesseursDAO
from modeconsole.view.gestionAdherents import GestionAdherent


class Menu:
    def __init__(self):
        self.gestionAdherents = GestionAdherent()
        self.gestionProfesseurs = GestionProfesseurs()

    def afficher(self):
        print("0 : Quitter l'application")
        print("1 : Afficher la liste des adherents")
        print("2 : Afficher la liste des professeurs")
        print("3 : Afficher la liste des grades d'un adherent")
        print("4 : Afficher la liste des diplomes d'un professeur")
        print("5 : Ajouter un adherent")
        print("6 : Ajouter un professeur")
        print("7 : Ajouter un grade à un adherent")
        print("8 : Ajouter un diplome à un professeur")
        print("9 : Ajouter a partir du csv test.csv")

    def run(self):
        fini = False
        while not fini:
            self.afficher()
            try:
                choix = int(input("Votre choix ? : "))
                if choix == 1:
                    self.gestionAdherents.afficherAdherents()
                elif choix == 2:
                    self.gestionProfesseurs.afficherProfesseurs()
                elif choix == 3:
                    self.gestionAdherents.afficherGradeAdherents()
                elif choix == 4:
                    self.gestionProfesseurs.afficherDiplome()
                elif choix == 5:
                    self.gestionAdherents.afficherAjoutAdherent()
                elif choix == 6:
                    self.gestionProfesseurs.afficherAjoutProfesseur()
                elif choix == 7:
                    self.gestionAdherents.afficherAjoutGradeAdherents()
                elif choix == 8:
                    self.gestionProfesseurs.afficherAjoutDiplome()
                elif choix == 9:
                    adherentDAO = AdherentsDAO()
                    professeurDAO = ProfesseursDAO()
                    try:
                        path = "test.csv"
                    except KeyboardInterrupt:
                        pass
                    except EOFError:
                        pass
                    else:
                        try:
                            f = open(path, "r")
                        except IOError:
                            print("Impossible d'ouvrir le fichier ", path)
                        line = f.readline()
                        while (line != "" and line != "\n"):
                            data = line.split(",")
                            try:
                                adherentDAO.insertWithLicence(data[0], data[1], data[2], datetime.strptime(data[3].rstrip(), "%d/%m/%Y"))
                                line = f.readline()
                            except ValueError as val:
                                print("Impossible d'ouvrir le fichier ", path, val)
                                line = ""
                        line = f.readline()
                        while (line != "" and line != "\n"):
                            data = line.split(",")
                            try:
                                professeurDAO.insertWithLicence(data[0], data[1], data[2], datetime.strptime(data[3].rstrip(), "%d/%m/%Y"))
                                line = f.readline()
                            except ValueError:
                                print("Impossible d'ouvrir le fichier ", path)
                                line = ""


                        f.close()
                else:
                    fini = True
            except ValueError as valueError:
                print("Mauvais choix ....")
                print("")

            except KeyboardInterrupt:
                try:
                    print("")
                    input("Faites ctrl + c une deuxieme fois pour quitter.")
                except KeyboardInterrupt:
                    fini = True


print("")
print("Merci d'avoir utiliser mon logiciel.")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
