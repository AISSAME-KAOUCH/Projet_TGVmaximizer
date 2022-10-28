from DAO.db_connection import DBConnection
from business_object.trajet import Trajet
import requests
from utils.singleton import Singleton

class TrajetDAO(metaclass=Singleton):
    
    """Classe permettant la communication avec notre base de données en ce qui concerne les trajets.
    Elle permet de récupérer des trajets depuis notre base de données mais aussi d'en ajouter. 
    """
    def find_max_id(self):
        request = "SELECT max(id) as maximum FROM trajet " 
                  
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request )
                resultat = cursor.fetchall()
            return resultat


    def find_by_depart(self, date_depart : str,heure_depart : str,ville_depart : str,ville_arrivee : str ) -> Trajet:

        """Fonction permettant de récupérer, dans la base de données, les trajets
        correspondant aux informations données, et de stocker les informations de ces trajets
        dans des objets Trajets.

        Parameters
        ----------
        date_depart : str
            Date de départ du trajet souhaité
        heure_depart : str
            Heure de départ du trajet souhaité
        ville_depart : str
            Ville de départ du trajet souhaité
        ville_arrivee : str
            Ville d'arrivée du trajet souhaité
        
        ----------
        Returns
        ----------
        list[Trajet] : liste des objets Trajets qui contiennent les informations des trajets 
        correspondants aux critères en paramètres. 
        """

        request = "SELECT * FROM trajet " \
                  "WHERE date = %(date_depart)s and heure_depart = %(heure_depart)s "\
                  "and ville_depart=%(ville_depart)s and  ville_arrivee=%(ville_arrivee)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"date_depart" : date_depart,"heure_depart" : heure_depart,"ville_depart" : ville_depart,"ville_arrivee" : ville_arrivee}
                )
                res = cursor.fetchall()

        tjs=[]
        if res :
            
            for t in res :
                trajet = Trajet(ville_depart = t['ville_depart'], 
                            id=t['id'],
                            date_depart= t['date'], 
                            heure_depart = t['heure_depart'],
                            ville_arrivee = t['ville_arrivee'], 
                            heure_arrivee = t['heure_arrivee'],
                            numero_train=t['numero_train'],
                            disponibilite_max=t['disponibilite_max']

                            )
                tjs+=[trajet]
                
        return tjs 
    def insert_trajets(self,trajets : list[Trajet]):
        
        """Fonction qui permet de stocker dans la base de données de nouveau trajets à partir
        d'objets métiers Trajet.
        
        Parameters
        ----------
        trajets : list[Trajet]
            Liste des trajets que l'on souhaite insérer dans la base de données.
            
        Returns
        -------
        None
        """

        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                for i in range(len(trajets)):
                    cursor.execute('INSERT INTO trajet (id,ville_depart,date,heure_depart,ville_arrivee,heure_arrivee,numero_train,disponibilite_max) '\
                        'VALUES (%(id)s, %(ville_depart)s,%(date_depart)s,%(heure_depart)s,%(ville_arrivee)s,%(heure_arrivee)s,%(numero_train)s,%(disponibilite_max)s)'\
                            ,{"id": trajets[i].id
                            , "ville_depart" : trajets[i].ville_depart
                            , "date_depart" : trajets[i].date_depart
                            , "heure_depart": trajets[i].heure_depart
                            , "ville_arrivee" : trajets[i].ville_arrivee
                            , "heure_arrivee" : trajets[i].heure_arrivee
                            , "numero_train" : trajets[i].numero_train
                            , "disponibilite_max" : trajets[i].disponibilite_max
                            })
