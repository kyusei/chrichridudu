import unittest

from DAO.EquipeDAO import AdherentsDAO


class TestAdherentsDAO(unittest.TestCase):

    def test_hasdoc(self):
        self.assertLess(10, len(AdherentsDAO.__doc__))

    def test_findById(self):
        self.adherentDAO = AdherentsDAO()
        self.assertIsNone(self.adherentDAO.findById(-1))
        self.assertIsNone(self.adherentDAO.findById(""))
        self.assertIsNone(self.adherentDAO.findById("dsdf"))

    def test_findAll(self):
        self.adherentDAO = AdherentsDAO()
        listesAdherent = self.adherentDAO.findAll()
        self.assertIsNotNone(listesAdherent)


if __name__ == '__main__':
    unittest.main()
