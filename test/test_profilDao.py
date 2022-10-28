from unittest import TestCase
import unittest
from DAO.profilDAO import ProfilDAO

class TestProfilDAO(TestCase):

    def test_find_by_id(self):
        profil_vide = ProfilDAO()
        email = "mail"
        profil = profil_vide.find_by_id(email)
        self.assertEqual(email, profil.email)

    def test_modifier_mot_de_passe(self):
        profil_dao = ProfilDAO()
        profil_modifie = Profil("Dupont", "Jean", "02-03-2000", "M", "jean.dupont@gmail.com", "super_mdp")
        updated = profil_dao.modifier_mot_de_passe(profil_modifie)
        self.assertTrue(updated)

    def test_modifier_profil(self):
        profil_dao = ProfilDAO()
        profil_modifie = Profil("Dupont", "Jean", "02-03-2000", "M", "jean.dupont@gmail.com", "super_mdp")
        updated = profil_dao.modifier_profil(profil_modifie)
        self.assertTrue(updated)

if __name__ == "__main__":
    unittest.main()

    