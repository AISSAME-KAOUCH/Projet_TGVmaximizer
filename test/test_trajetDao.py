from unittest import TestCase
import unittest
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet


class TestTrajetDAO(TestCase):

    # def test_find_by_depart(self):
    #     trajet_vide = TrajetDAO()
    #     date_depart = "30-10-2022"
    #     heure_depart = "20:00:00"
    #     ville_depart = "Paris"
    #     ville_arrivee = "Bordeaux"
    #     trajet = trajet_vide.find_by_depart(date_depart, heure_depart, ville_depart, ville_arrivee)
    #     self.assertEqual(date_depart, trajet.date_depart)
    #     self.assertEqual(heure_depart, trajet.heure_depart)
    #     self.assertEqual(ville_depart, trajet.ville_depart)
    #     self.assertEqual(ville_arrivee, trajet.ville_arrivee)

    def test_insert_trajet(self):
        trajet_dao = TrajetDAO()
        trajet = []
        test = Trajet(None, "Paris", "30-10-2022", "20:00:00", "Bordeaux", None, None, None)
        trajet.append(test)
        insert = trajet_dao.insert_trajets(trajet)


if __name__ == "__main__":
    unittest.main()