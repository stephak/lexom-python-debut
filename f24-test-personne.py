#f24-test_personne.py 
import unittest
from personne import Personne


class Personnetest(unittest.TestCase):
    def test_simple_prenom(self):
        self.obj = Personne(prenom='Guilhem', dob='17/04/1998')
        self.assertEqual(self.obj.prenom, "Guilhem")

    def test_simple_age(self):
        self.obj = Personne(prenom='Guilhem',dob='17/04/1998')
        self.assertEqual(self.obj.age(), 21)

if __name__ == '__main__':
    unittest.main()