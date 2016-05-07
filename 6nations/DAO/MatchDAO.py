from DAO.MainDAO import DAO
from models import Match
from datetime import date


class MatchDAO(DAO):
    def getAllMatch(self):
        Tmatch = []
        for match in self.session.query(Match):
            Tmatch.append(match)
        return Tmatch

    def getByIdEquipes(self, id_equipe1, id_equipe2):
        return self.session.query(Match).filter('match.idEquipe1' == id_equipe1, 'match.idEquipe2' == id_equipe2).one_or_none()


    def addMatch(self, lieu, date, id_equipe1, id_equipe2):
        match = Match(lieu, date, id_equipe1, id_equipe2)
        self.session.add(match)
        self.session.commit()
