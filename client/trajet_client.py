import os
import requests
from business_object.trajet import Trajet


HOST_WEBSERVICE="https://data.sncf.com"
END_POINT="/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&facet=date&facet=origine&facet=destination&facet=od_happy_card"

class Trajetclient :
    """
    Classe qui permet de communiquer avec l'API SNCF et de récupérer les trajets.
    """

    def get_trajets(self, annee, mois, jour, ville_depart, ville_arrivee = None, id_initial = None) :
        """ 
        Fonction qui permet de récupérer les trajets sur l'API SNCF correspondant aux critères
        entrés en paramètres

        Parameters
        ----------
        annee : str
            annee du trajet
        mois : str
            mois du trajet
        jour : str
            jour du trajet
        ville_depart : str
            ville de laquelle part le train correspondant au trajet
        ville_arrivee : str
            ville dans laquelle arrive le train correspondant au trajet
        id_initial = int
            identifiant du trajet
        
        Returns 
        -------
        trajets : Trajet
            Les trajets correspondant aux critères de la recherche
        """

        req = requests.get(f"{HOST_WEBSERVICE}{END_POINT}&refine.date={annee}%2F{mois}%2F{jour}&refine.origine={ville_depart}&refine.destination={ville_arrivee}")
        dic=req.json()
        resultat=dic['records']
        trajets=[]
        j=id_initial+1
        for i in resultat :
            tj=Trajet(j,i['fields']['origine'],i['fields']['date'],i['fields']['heure_depart'],i['fields']['destination'],i['fields']['heure_arrivee'],i['fields']['train_no'],i['fields']['od_happy_card'])
            trajets.append(tj)  
            j+=1
        return trajets

    def get_trajets2(self, ville_depart, id_initial) :

        """Fonction qui permet de récupérer les trajets si seule la ville de départ est renseignée
        
        Parameters 
        ----------
        ville_depart : str 
            ville de laquelle part le train correspondant au trajet
        id_initial : int 
            identifiant du trajet

        Returns
        -------
        trajets : Trajet
            Les trajets correspondant aux critères de la recherche
        """

        req = requests.get(f"{HOST_WEBSERVICE}{END_POINT}&refine.origine={ville_depart}")
        dic=req.json()
        resultat=dic['records']
        trajets=[]
        j=id_initial+1
        for i in resultat :
            tj=Trajet(j,i['fields']['origine'],i['fields']['date'],i['fields']['heure_depart'],i['fields']['destination'],i['fields']['heure_arrivee'],i['fields']['train_no'],i['fields']['od_happy_card'])
            trajets.append(tj)  
            j+=1
        return trajets



