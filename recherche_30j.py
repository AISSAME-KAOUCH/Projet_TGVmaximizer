from recherche import Recherche
from  DAO import rechercheDAO 
class Recherche_30j(Recherche):

    def __init__(self,profil: Profil,trajet: Trajet) -> None:
        super().__init__()
        self.profil=profil
        self.trajet=trajet

    def recherche(self,trajet):
        return rechercheDAO.find_by_id(trajet)
    
    def sauvegarder(self, trajet, profil):
        rechercheDAO.sauvegarder(trajet, profil)
    
    
        


