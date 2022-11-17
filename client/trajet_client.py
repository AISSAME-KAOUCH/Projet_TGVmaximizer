import os
import requests
from business_object.trajet import Trajet


HOST_WEBSERVICE="https://data.sncf.com"
END_POINT="/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&facet=date&facet=origine&facet=destination&facet=od_happy_card"

class Trajetclient :

    """Classe qui permet de communiquer avec l'API SNCF et de récupérer les trajets."""

    #def __init__(self) -> None:
    #    self.__HOST =os.environ["HOST_WEBSERVICE"]

    def get_trajets(self, annee, mois, jour, ville_d, ville_arrivee = None, id_initiale = None) :

        """ Fonction qui permet de récupérer les trajets sur l'API SNCF correspondant aux critères
        entrés en paramètres

        Parameters
        ----------
        annee : str
            annee du trajet
        mois : str
            mois du trajet
        jour : str
            jour du trajet
        ville_d : str
            ville de laquelle part le train correspondant au trajet
        ville_arrivee : str
            ville dans laquelle arrive le train correspondant au trajet
        id_initiale = int
            identifiant du trajet
        
        Returns 
        -------
        None
        """

        req = requests.get(f"{HOST_WEBSERVICE}{END_POINT}&refine.date={annee}%2F{mois}%2F{jour}&refine.origine={ville_d}&refine.destination={ville_arrivee}")
        dic=req.json()
        resultat=dic['records']
        trajets=[]
        j=id_initiale+1
        for i in resultat :
            #print((i['fields']['origine'],i['fields']['destination'],i['fields']['heure_depart'],i['fields']['heure_arrivee']))
            tj=Trajet(j,i['fields']['origine'],i['fields']['date'],i['fields']['heure_depart'],i['fields']['destination'],i['fields']['heure_arrivee'],i['fields']['train_no'],i['fields']['od_happy_card'])
            trajets.append(tj)  
            j+=1
        return trajets
        
if __name__=='__main__' :
    trajet=Trajetclient()
    resultat=trajet.get_trajets('2022', '11', '02', 'NANTES', 'LE+MANS')
    for tj in resultat :
        print(tj.__str__())

