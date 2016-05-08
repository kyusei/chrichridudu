# -*-coding:UTF-8 -*
from datetime import datetime
from modeconsole.view.gestion import GestionMatch
from modeconsole.view.gestion import GestionScore
from DAO.EquipeDAO import EquipeDAO
from DAO.MatchDAO import MatchDAO
from DAO.ScoreDAO import ScoreDAO
from modeconsole.view.gestion import GestionEquipe


class Menu:
    def __init__(self):
        self.gestionMatch = GestionMatch()
        self.gestionScore = GestionScore()
        self.gestionEquipe = GestionEquipe()

    def afficher(self):
        print("0 : Quitter l'application")
        print("1 : Afficher la liste des Matchs")
        print("2 : Afficher la liste des Equipes")
        print("3 : Ajouter un match")
        print("4 : Ajouter une equipe")
        print("5 : Ajouter un score pour une équipe et un match")
        print("6 : Afficher le score d'un match pour une equipe choisie")

    def run(self):
        fini = False
        while not fini:
            self.afficher()
            try:
                choix = int(input("Votre choix ? : "))
                if choix == 1:
                    self.gestionMatch.afficherMatchs()
                elif choix == 2:
                    self.gestionEquipe.afficherAllEquipe()
                elif choix == 3:
                    self.gestionMatch.afficherAddMatch()
                elif choix == 4:
                    self.gestionEquipe.addEquipe()
                elif choix == 5:
                    self.gestionScore.afficherAjoutScore()
                elif choix == 6:
                    self.gestionScore.afficherScoreEquipeByMatch()
                else:
                    fini = True


            except KeyboardInterrupt:
                try:
                    print("")
                    input("Faites ctrl + c une deuxieme fois pour quitter.")
                except KeyboardInterrupt:
                    fini = True


if __name__ == "__main__":
    menu = Menu()
    menu.run()
