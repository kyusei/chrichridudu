import unittest

from models import Professeur
from service.ServiceProfesseur import ServiceProfesseur


class TestServiceProfesseur(unittest.TestCase):

    def test_HasDoc(self):
        self.assertLess(10, len(ServiceProfesseur.__doc__))

    def test_init(self):
        self.assertRaises(AttributeError, ServiceProfesseur, None)
        self.assertRaises(AttributeError, ServiceProfesseur, 1)
        self.assertRaises(AttributeError, ServiceProfesseur, "")
        self.assertIsNotNone(ServiceProfesseur(Professeur("test", "test", "test")))


if __name__ == '__main__':
    unittest.main()
