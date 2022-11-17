from unittest import TestCase
import unittest
from DAO.profilDAO import ProfilDAO
from business_object.profil import Profil

class TestProfilDAO(TestCase):

    def test_create_profil(self):
        profil_dao = ProfilDAO()
        profil = Profil("M", "Jean", "Dupont", "02-03-2000", "jean.dupont@gmail.com", "super_mdp")
        created = profil_dao.create_profil(profil)

    def test_find_by_id(self):
        profil_vide = ProfilDAO()
        email = "jean.dupont@gmail.com"
        profil = profil_vide.find_by_id(email)
        self.assertEqual(email, profil.email)

    def test_modifier_mot_de_passe(self):
        profil_dao = ProfilDAO()
        profil_modifie = Profil("M", "Jean", "Dupont", "02-03-2000", "jean.dupont@gmail.com", "super_mdp2")
        updated = profil_dao.modifier_mot_de_passe(profil_modifie)
        self.assertTrue(updated)

    def test_modifier_profil(self):
        profil_dao = ProfilDAO()
        profil_modifie = Profil("Mme", "Jeanne", "Duponte", "02-03-2002", "jean.dupont@gmail.com", "super_mdp")
        updated = profil_dao.modifier_profil(profil_modifie)
        self.assertTrue(updated)


    if __name__ == "__main__":
        unittest.main()

    