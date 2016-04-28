from datetime import date

from DAO.MainDAO import DAO
from models import Score


class ScoreDAO(DAO):
    def getAllScores(self):
        Tscore = []
        for score in self.session.query(Score):
            diplomes.append(score)
        return Tscore

    def getByMatchAndTeam(self,id_equipe, id_match):
        return self.session.query(Score).filter(Score.idEquipe == id_equipe,
                                                Score.idMatch == id_match).one_or_none()

    def addScoreMatchForTeam(self, idMatch, idEquipe, typePoint, temps):
        score = Score(idMatch, idEquipe, typePoint, temps)
        self.session.add(score)
        self.session.commit()