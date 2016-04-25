from kendoDAO.AbstractDAO import DAO
from models import Professeur


class ProfesseursDAO(DAO):
    def findAll(self):
        professeurs = []
        for professeur in self.session.query(Professeur):
            professeurs.append(professeur)
        return professeurs

    def findById(self, id):
        return self.session.query(Professeur).filter(Professeur.licence == id).one_or_none()

    def insert(self, nom, prenom, dateNaissance):
        professeur = Professeur(nom, prenom, dateNaissance)
        self.session.add(professeur)
        self.session.commit()

    def insertWithLicence(self, licence, nom, prenom, dateNaissance):
        professeur = Professeur(nom, prenom, dateNaissance, licence)
        self.session.add(professeur)
        self.session.commit()
