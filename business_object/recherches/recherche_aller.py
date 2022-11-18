from business_object.recherches.abstract_recherche import AbstractRecherche
from DAO.rechercheDAO import RechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient
from business_object.profil import Profil

class Recherche_aller(AbstractRecherche):

    def __init__(self, profil: Profil, trajet: Trajet) -> None:
        super().__init__()
        self.profil = profil
        self.trajet = trajet

    def find_id_trajet(self,trajet : Trajet):
        trajetdao = TrajetDAO()
        id = trajetdao.find_id(trajet)
        return id

    def recherche(self):
        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient= Trajetclient()
        jour = self.trajet.date_depart[:2] # On tire les informations
        mois = self.trajet.date_depart[3:5]# dont on a besoin 
        annee = self.trajet.date_depart[6:10] # de l'attribut date_depart
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets(annee, mois, jour, self.trajet.ville_depart, self.trajet.ville_arrivee,id_initial)
        trajetdao.insert_trajets(trajets)
        resultat_req =trajetdao.find_by_depart(self.trajet.date_depart, self.trajet.heure_depart, self.trajet.ville_depart, self.trajet.ville_arrivee)
        return resultat_req
    
    def sauvegarder(self):
        return None

    def creer_alerte(self, choix):
        if choix == "oui":
            rechercheDAO.creer_alerte(self.trajet, self.profil)

    
        


