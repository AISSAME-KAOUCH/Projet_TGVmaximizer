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

    def recherche(self,trajet : Trajet):
        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient= Trajetclient()
        jour = trajet.date_depart[:2] # On tire les informations
        mois = trajet.date_depart[4:6]# dont on a besoin 
        annee = trajet.date_depart[8:12] # de l'attribut date_depart
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets(annee, mois, jour, trajet.ville_depart, trajet.ville_arrivee,id_initial)
        trajetdao.insert_trajets(trajets)
        resultat_req =trajetdao.find_by_depart(trajet.date_depart, trajet.heure_depart, trajet.ville_depart, trajet.ville_arrivee)
        for trajet in resultat_req :
            print(trajet)
    
    def sauvegarder(self):
        return None

    def creer_alerte(self, choix):
        if choix == "oui":
            rechercheDAO.creer_alerte(self.trajet, self.profil)

profil = Profil("Dupont", "Jean", "02-03-1980", "M", "jean.dupont@gmail.com", "first_mdp")

trajet = Trajet('0','Paris', '10-01-2022', '07:00', 'Rennes', '', '0', 'oui')
rech = Recherche_aller(profil, trajet)
    
        


