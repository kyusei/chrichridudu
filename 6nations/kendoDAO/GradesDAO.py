from kendoDAO.AbstractDAO import DAO
from models import Grade
from datetime import date


class GradesDAO(DAO):
    def findAll(self):
        grades = []
        for grade in self.session.query(Grade):
            grades.append(grade)
        return grades

    def findByIdAdherent(self, idAdherent):
        grades = []
        for grade in self.session.query(Grade).filter(Grade.idAdherent == idAdherent):
            grades.append(grade)
        return grades
    def insertGrade(self, libelle, idAdherent):
        grade = Grade(libelle, idAdherent, date.today())
        self.session.add(grade)
        self.session.commit()
