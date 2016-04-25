from datetime import date

from kendoDAO.AbstractDAO import DAO
from models import Diplome


class DiplomesDAO(DAO):
    def findAll(self):
        diplomes = []
        for diplome in self.session.query(Diplome):
            diplomes.append(diplome)
        return diplomes

    def findByIdprofesseur(self,idProfesseur):
        diplomes = []
        for diplome in self.session.query(Diplome).filter(Diplome.idProfesseur == idProfesseur):
            diplomes.append(diplome)
        return diplomes

    def insert(self, titre, idProfesseur):
        diplome = Diplome(titre, idProfesseur, date.today())
        self.session.add(diplome)
        self.session.commit()