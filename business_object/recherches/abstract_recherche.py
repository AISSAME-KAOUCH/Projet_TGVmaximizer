from abc import ABC
class AbstractRecherche(ABC):

    """Classe abstraite pour les recherches """
    
    def __init__(self) -> None:
        super().__init__()
    
    def recherche(self):
        pass
    
    def sauvegarder(self):
        pass

    def creer_alerte(self):
        pass

    def __str__(self) -> str:
        return super().__str__()

    

    
        