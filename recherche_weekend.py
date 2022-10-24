from recherche import Recherche
from  DAO import rechercheDAO 
class Recherche_weekend(Recherche):

    def __init__(self, profil: Profil, trajet: Trajet) -> None:
        super().__init__()
        self.profil = profil
        self.trajet = trajet

    def recherche(self, trajet):
        return rechercheDAO.find_by_id(trajet)
    
    def sauvegarder(self, trajet, profil):
        rechercheDAO.sauvegarder(trajet, profil)
    
    def creer_alerte(self, trajet, profil, choix):
        if choix == "oui":
            rechercheDAO.creer_alerte(trajet, profil)
    
        


