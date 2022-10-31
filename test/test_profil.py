from unittest import TestCase
import unittest
from business_object.profil import Profil

class TestProfil(TestCase):

    def test_modifier_mdp(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "first_mdp")
        nv_mdp = "Second_mdp"
        profil.modifier_mdp(nv_mdp)
        self.assertEqual(nv_mdp, profil._mot_de_passe)

    def test_modifier_nom(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "super_mdp")
        nv_nom = "Rousseau"
        profil.modifier_nom(nv_nom)
        self.assertEqual(nv_nom, profil._nom)

    def test_modifier_prenom(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "super_mdp")
        nv_prenom = "Robert"
        profil.modifier_prenom(nv_prenom)
        self.assertEqual(nv_prenom, profil._prenom)

    def test_modifier_civilite(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "super_mdp")
        nv_civilite = "Mme"
        profil.modifier_civilite(nv_civilite)
        self.assertEqual(nv_civilite, profil._civilite)

    def test_modifier_date_de_naissance(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "super_mdp")
        nv_date = "04-07-1987"
        profil.modifier_date_de_naissance(nv_date)
        self.assertEqual(nv_date, profil._date_de_naissance)

    def test_email(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "super_mdp")
        nv_email = "email.update@gmail.com"
        profil.modifier_email(nv_email)
        self.assertEqual(nv_email, profil.email)

    def test_modifier_profil(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-1980", "jean.dupont@gmail.com", "super_mdp")
        nv_nom = "Durant"
        profil.modifier_profil()
        self.assertEqual(nv_nom, profil._nom)

    def test_type_abonnement(self):
        profil = Profil("M", "Jean", "Dupont", "02-03-2000", "jean.dupont@gmail.com", "super_mdp")
        self.assertEqual(profil.type_abonnement(), "jeune")

    # def test_str(self): 
    #     profil = Profil("Dupont", "Jean", "02-03-1980", "M", "jean.dupont@gmail.com", "super_mdp")
    #     res = 'Profil de M. Dupont Jean :\n Email: jean.dupont@gmail.com \n Date de naissance : 02-03-1980 ?'
    #     self.assertEqual(profil.__str__(), res)
    # Problème avec l'affichage du test 

    
if __name__ == "__main__":
    unittest.main()