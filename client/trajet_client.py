import os
import requests


HOST_WEBSERVICE="https://data.sncf.com"
END_POINT="/api/records/1.0/search/?dataset=tgvmax&q=&sort=-date&facet=date&facet=origine&facet=destination&facet=od_happy_card"
class Trajetclient :
    #def __init__(self) -> None:
    #    self.__HOST =os.environ["HOST_WEBSERVICE"]

    def get_trajets(self, annee,mois,jour,ville_d,ville_arrivee) :
        req = requests.get(f"{HOST_WEBSERVICE}{END_POINT}&refine.date={annee}%2F{mois}%2F{jour}&refine.origine={ville_d}&refine.destination={ville_arrivee}")
        dic=req.json()
        resultat=dic['records']
        for i in resultat :
            print((i['fields']['origine'],i['fields']['destination'],i['fields']['heure_depart'],i['fields']['heure_arrivee']))

if __name__=='__main__' :
    trajet=Trajetclient()
    trajet.get_trajets('2022','11','02',"NANTES","LE+MANS")

