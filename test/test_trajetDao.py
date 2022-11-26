from unittest import TestCase
import unittest
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
import datetime


class TestTrajetDAO(TestCase):

    def test_insert_trajet(self):
        trajet_dao = TrajetDAO()
        trajet = []
        test = Trajet(id = 48, ville_depart = "Paris", date_depart = "30-10-2022", heure_depart = "20:00:00", ville_arrivee = "Bordeaux", heure_arrivee = "22:00:00", disponibilite_max = 'OUI')
        trajet.append(test)
        insert = trajet_dao.insert_trajets(trajet)

    def test_find_by_depart(self):
        trajet_vide = TrajetDAO()
        date_depart = "30-10-2022"
        heure_depart = "20:00:00"
        ville_depart = "Paris"
        ville_arrivee = "Bordeaux"
        trajet = trajet_vide.find_by_depart(date_depart, heure_depart, ville_depart, ville_arrivee)
        self.assertEqual(datetime.time(20, 0), trajet[0].heure_depart)
        self.assertEqual(ville_depart, trajet[0].ville_depart)
        self.assertEqual(ville_arrivee, trajet[0].ville_arrivee)

if __name__ == "__main__":
    unittest.main()