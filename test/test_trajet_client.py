from unittest import TestCase, mock
import unittest
from client.trajet_client import Trajetclient
import os

# @mock.patch.dict(os.environ, {"HOST_WEBSERVICE": "https://data.sncf.com"})
class TestTrajetClient(TestCase):

    def test_get_trajets(self):
        test = Trajetclient()
        annee = "2022"
        mois = "11"
        jour = "25"
        ville_d = "NANTES"
        ville_arrivee = "LE+MANS"
        trajets = test.get_trajets(annee, mois, jour, ville_d, ville_arrivee)
        print(trajets)
        # self.assertEqual(email, profil.email)

if __name__ == "__main__":
    unittest.main()
