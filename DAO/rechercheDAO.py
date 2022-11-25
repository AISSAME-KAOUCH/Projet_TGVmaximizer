from DAO.db_connection import DBConnection
from business_object.profil import Profil
import requests
from business_object.recherches.abstract_recherche import AbstractRecherche
from utils.singleton import Singleton
from business_object.trajet import Trajet

class RechercheDAO(metaclass=Singleton):
    def create(self,profil : Profil, trajet : Trajet) :
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("INSERT INTO recherche(id, email, date, heure_depart, ville_depart)"\
                    "VALUES (%(id)s, %(email)s, %(date)s, %(heure)s, %(ville_de_depart)s) "\
                    , {"id" : trajet.id
                    , "email" : profil.email
                    , "date" : trajet.date_depart
                    , "heure" : trajet.heure_depart
                    , "ville_de_depart" : trajet.ville_depart})

    def delete(self) : 
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("DELETE FROM recherche WHERE id = %(id)s and email = %(email)s "\
                    , {"id" : self.trajet.id
                    , "email" : self.profil.email})


    
    def update(self):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("UPDATE recherche SET email = %(email)s, date = %(date)s, heure = %(heure)s, ville_de_depart = %(ville_de_depart)s"\
                    "WHERE id = %(id)s"\
                    , {"email" : self.profil.email
                    , "date" : self.trajet.date
                    , "heure" : self.trajet.heure_depart
                    ,"ville_de_depart" : self.trajet.ville_depart})

    def creer_alerte(self, choix : str):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("UPDATE recherche SET choix_alerte = %(choix)s"\
                    "WHERE id = %(id)s"\
                    , {'choix': choix
                    , 'id' : self.trajet.id})
#creer colonne alerte

