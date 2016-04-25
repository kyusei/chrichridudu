# coding=utf-8
from kendoDAO.AbstractDAO import DAO
from models import Adherent


class AdherentsDAO(DAO):
    """
    Cette Classe est une facade avec la base de données sqlite
    Elle communique avec la base pour la classe Adherent
    """

    def findAll(self):
        """
        Permet de récuperer tous les adherents
        Returns List<Adherent> : list d'adherent
        """
        adherents = []
        for adherent in self.session.query(Adherent):
            adherents.append(adherent)
        return adherents

    def insertWithLicence(self, licence, nom, prenom, dateNaissance):
        adherent = Adherent(nom, prenom, dateNaissance, licence)
        self.session.add(adherent)
        self.session.commit()

    def insert(self, nom, prenom, dateNaissance):
        """
        Permet d'inserer un étudiant en base
        Args nom : String le nom de l'adherent
        Args prenom : String le prenom
        Args dateNaissane : DateTime date de naissance
        Returns None
        """
        adherent = Adherent(nom, prenom, dateNaissance)
        self.session.add(adherent)
        self.session.commit()


    def findById(self, id):
        """
        Permet de recuperer un etudiant
        Si il ne trouve pas d'étudiant renvoie None
        Args id : Integer
        Returns Etudiant | None
        """
        return self.session.query(Adherent).filter(Adherent.licence == id).one_or_none()