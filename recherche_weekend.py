from recherche import Recherche
from  DAO import rechercheDAO 
class Recherche_weekend(Recherche):

    def __init__(self, profil: Profil, trajet: Trajet) -> None:
        super().__init__()
        self.profil = profil
        self.trajet = trajet

    def recherche(self):
        return rechercheDAO.find_by_id(self.trajet)
    
    def sauvegarder(self):
        rechercheDAO.sauvegarder(self.trajet, self.profil)
    
    def creer_alerte(self, choix):
        if choix == "oui":
            rechercheDAO.creer_alerte(self.trajet, self.profil)
    
        


