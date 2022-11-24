from business_object.recherches.abstract_recherche import AbstractRecherche
from DAO.rechercheDAO import RechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient
from business_object.profil import Profil

class Recherche_aller_retour(AbstractRecherche):

    """Classe qui permet d'effectuer une recherche pour un aller-retour"""

    

    def __init__(self, profil: Profil, trajet_aller: Trajet, trajet_retour: Trajet) -> None:

        """Constructeur la recherche d'un trajet aller-retour
        
        Parameters
        ----------
        trajet_aller : Trajet
            Le trajet d'aller
        trajet_retour : Trajet
            Le trajet retour
        profil : Profil
            Le profil qui effectue la recherche
        """

        super().__init__()
        self.trajet_aller = trajet_aller
        self.trajet_retour = trajet_retour
        self.profil=profil

    def recherche(self):

        """Classe qui permet d'effectuer la recherche pour un aller-retour
        
        Returns
        --------
        resultat_req1 : Trajet
            Le trajet aller souhaité par l'utilisateur
        resultat_req2 : Trajet
            Le trajet retour souhaité par l'utilisateur
        """

        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient= Trajetclient()
        jour = self.trajet_aller.date_depart[:2] # On tire les informations
        mois = self.trajet_aller.date_depart[3:5]# dont on a besoin 
        annee = self.trajet_aller.date_depart[6:10] # de l'attribut date_depart
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets(annee, mois, jour, self.trajet_aller.ville_depart, self.trajet_aller.ville_arrivee,id_initial)
        trajetdao.insert_trajets(trajets)
        for j in trajets :
            RechercheDAO().create(self.profil,j)
        if self.trajet_aller.heure_depart=='' :
            resultat_req1 =trajetdao.find_by_depart2(self.trajet_aller.date_depart, self.trajet_aller.heure_depart, self.trajet_aller.ville_depart, self.trajet_aller.ville_arrivee)
        else :
            resultat_req1 =trajetdao.find_by_depart2(self.trajet_aller.date_depart, self.trajet_aller.heure_depart, self.trajet_aller.ville_depart, self.trajet_aller.ville_arrivee)
        jour_retour = self.trajet_retour.date_depart[:2] # On tire les informations
        mois_retour = self.trajet_retour.date_depart[3:5]# dont on a besoin 
        annee_retour = self.trajet_retour.date_depart[6:10] # de l'attribut date_depart
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets(annee_retour, mois_retour, jour_retour, self.trajet_retour.ville_depart, self.trajet_retour.ville_arrivee,id_initial)
        trajetdao.insert_trajets(trajets)
        for j in trajets :
            RechercheDAO().create(self.profil,j)
        if self.trajet_retour.heure_depart=='' :
            resultat_req2 =trajetdao.find_by_depart2(self.trajet_retour.date_depart, self.trajet_retour.heure_depart, self.trajet_retour.ville_depart, self.trajet_retour.ville_arrivee)
        else :
            resultat_req2 =trajetdao.find_by_depart(self.trajet_retour.date_depart, self.trajet_retour.heure_depart, self.trajet_retour.ville_depart, self.trajet_retour.ville_arrivee)
        # Affichage intégré         
        return (resultat_req1,resultat_req2)
    
    def sauvegarder(self):

        """Classe pour sauvegarder les trajets associés au profil"""

        rechercheDAO.sauvegarder(self.trajet, self.profil)
    
    def creer_alerte(self):

        """Classe pour créer une alerte mail si un trajet correspondant aux critères est disponible"""

        rechercheDAO.creer_alerte(self.trajet, self.profil)
    
        


