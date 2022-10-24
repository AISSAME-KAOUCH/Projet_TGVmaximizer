from abc import ABC
class Recherche(ABC):
    
    def __init__(self) -> None:
        super().__init__()
    
    def recherche(self, trajet):
        pass
    
    def sauvegarder(self, trajet):
        pass

    def creer_alerte(self, choix):
        pass

    def __str__(self) -> str:
        return super().__str__()

    

    
        