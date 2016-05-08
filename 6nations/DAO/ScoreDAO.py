from datetime import date

from DAO.MainDAO import DAO
from models import Score


class ScoreDAO(DAO):
    def getAllScores(self):
        Tscore = []
        for score in self.session.query(Score):
            Tscore.append(score)
        return Tscore

    def getByMatchAndTeam(self,id_equipe, id_match):
        return self.session.query(Score).filter(Score.idEquipe == id_equipe,
                                                Score.idMatch == id_match).one_or_none()

    def addScoreMatchForTeam(self, idMatch, idEquipe, typePoint, temps):
        score = Score(idMatch, idEquipe, typePoint, temps)
        self.session.add(score)
        self.session.commit()

    def getNbPointsFromType (self, typePoint):
        nbPoint = 0
        if (typePoint == "essai" ):
            nbPoint=5
        elif (typePoint=="penalite"):
            nbPoint=3
        elif (typePoint == "drop"):
            nbPoint=3
        elif (typePoint == "transformation"):
            nbPoint=2

        return nbPoint;