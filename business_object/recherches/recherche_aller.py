from abstract_recherche import AbstractRecherche
from  DAO import rechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient

class Recherche_aller(AbstractRecherche):

    def __init__(self, profil: Profil, trajet: Trajet) -> None:
        super().__init__()
        self.profil = profil
        self.trajet = trajet

    def find_id_trajet(self,trajet : Trajet):
        trajetdao = TrajetDAO()
        id = trajetdao.find_id(trajet)
        return id

    def recherche(self,trajet : Trajet):
        trajetdao = TrajetDAO()
        trajetclient= Trajetclient()
        jour = trajet.date_depart[:2]
        mois = trajet.date_depart[4:6]
        annee = trajet.date_depart[8:12]
        trajets = trajetclient.get_trajets(annee, mois, jour, trajet.ville_depart, trajet.ville_arrivee)
        trajetdao.insert_trajets(trajets)
        resultat_req =trajetdao.find_by_depart(trajet.date_depart, trajet.heure_depart, trajet.ville_depart, trajet.ville_arrivee)
        for trajet in resultat_req :
            print(trajet)
    
    def sauvegarder(self):
        return None

    def creer_alerte(self, choix):
        if choix == "oui":
            rechercheDAO.creer_alerte(self.trajet, self.profil)

profil = Profil()    
trajet = Trajet('Paris', '10-01-2022', '07:00', 'Rennes', '', '0', 'oui')
rech = Recherche_aller(profil, trajet)
    
        


