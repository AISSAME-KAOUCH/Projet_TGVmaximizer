from unittest import TestCase
import unittest
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.trajet import Trajet
from business_object.profil import Profil

class TestRechercheAller(TestCase):

    def test_find_id_trajet(self):
        profil = Profil("Dupont", "Jean", "02-03-1980", "M", "jean.dupont@gmail.com", "first_mdp")
        trajet = Trajet('0','RENNES', '08-12-2022', '09:35:00', 'LAVAL', '12:00:00', '22', 'oui')
        recherche_aller = Recherche_aller(profil, trajet)
        res = recherche_aller.find_id_trajet(trajet)
        self.assertEqual(res, '0')

#    def test_recherche(self):
#    def test_sauvegarder(
#    def test_creer_alerte()

if __name__ == "__main__":
    unittest.main()