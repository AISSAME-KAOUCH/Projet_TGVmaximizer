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

    def delete(self, recherche) : 
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("DELETE FROM recherche WHERE id = %(id)s and email = %(email)s "\
                    , {"id" : trajet.id
                    , "email" : profil._email})

    def save(self, profil: Profil, trajet) :
        self.create(profil, trajet)

    def find_by_id(self, trajet : Trajet):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("SELECT * FROM recherche JOIN trajet ON trajet.id = recherche.id "\
                    "WHERE recherche.id = %(id)s"
                    , {"id": trajet.id})
        return cursor.fetchall()

    
    def update(self, recherche):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("UPDATE recherche SET email = %(email)s, date = %(date)s, heure = %(heure)s, ville_de_depart = %(ville_de_depart)s"\
                    "WHERE id = %(id)s"\
                    , {"email" : recherche.email
                    , "date" : recherche.date
                    , "heure" : recherche.heure
                    ,"ville_de_depart" : recherche.depart})

    def creer_alerte(self, recherche, choix : str):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute("UPDATE recherche SET choix_alerte = %(choix)s"\
                    "WHERE id = %(id)s"\
                    , {'choix': choix
                    , 'id' : recherche.id})
#creer colonne alerte

