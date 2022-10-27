from DAO.db_connection import DBConnection
from business_object.trajet import Trajet
import requests
from utils.singleton import Singleton

class TrajetDAO(metaclass=Singleton):
    
    def find_by_depart(self, date_depart : str,heure_depart : str,ville_depart : str,ville_arrivee ) -> Trajet:

        request = "SELECT * FROM profil" \
                  "WHERE date_depart = %(date_depart)s and heure_depart = %(heure_depart)s and "\
                  "and ville_depart=%(ville_depart)s and  ville_arrivee=%(ville_arrivee)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"date_depart" : date_depart,"heure_depart" : heure_depart,"ville_depart" : ville_depart,"ville_arrivee" : ville_arrivee}
                )
                res = cursor.fetchall()
        trajets=[]
        if res :
            for t in res :
                trajet = Trajet(ville_depart = t['ville_depart'], 
                            id=t['id'],
                            date_depart = t['date_depart'], 
                            heure_depart = t['heure_depart'],
                            ville_arrivee = t['ville_arrivee'],
                            date_arrivee = t['date_arrivee'], 
                            heure_arrivee = t['heure_arrivee'],
                            numero_train=t['numero_train']
                            )
                trajets=trajets.append(trajet)   
        return trajets

    def insert_trajets(self,trajets : list[Trajet]):
        
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                for i in range(len(trajets)):
                    cursor.execute('INSERT INTO trajet (id,ville_depart,date_depart,heure_depart,ville_arrivee,date_arrivee,heure_arrivee,numero_train) '\
                        'VALUES (%(id)s, %(ville_depart)s,%(date_depart)s,%(heure_depart)s,%(ville_arrivee)s,%(date_arrivee)s,%(heure_arrivee)s,%(numero_train)s)'\
                            ,{"id": trajets[i].id
                            , "ville_depart" : trajets[i].ville_depart
                            , "date_depart" : trajets[i].date_depart
                            , "heure_depart": trajets[i].heure_depart
                            , "ville_arrivee" : trajets[i].ville_arrivee
                            , "date_arrivee" : trajets[i].date_arrivee
                            , "heure_arrivee" : trajets[i].heure_arrivee
                            , "numero_train" : trajets[i].numero_train
                            })
