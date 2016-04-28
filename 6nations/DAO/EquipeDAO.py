# coding=utf-8
from DAO.MainDAO import DAO
from models import Equipe


class EquipeDAO(DAO):


    def getAllEquipe(self):
        Tequipe = []
        for equipe in self.session.query(Equipe):
            Tequipe.append(equipe)
        return Tequipe

    def addEquipe(self, pays, classement, goalAverage, nbGagne, nbPerdu, nbNul):

        equipe = Equipe(pays, classement, goalAverage, nbGagne, nbPerdu, nbNul)
        self.session.add(equipe)
        self.session.commit()


    def getEquipe(self, id):

        return self.session.query(Equipe).filter(Equipe.idEquipe== id).one_or_none()