from business_object.recherches.abstract_recherche import AbstractRecherche
from DAO.rechercheDAO import RechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient
from business_object.profil import Profil
class Recherche_30j(AbstractRecherche):

    """Classe qui permet de rechercher dans la base de données les trajets demandés"""

    def __init__(self, profil, ville_depart, date):

        """Constructeur permettant l'instanciation d'une recherche pour un profil renseigné

        Parameters
        ---------- 
        profil : Profil 
            Un objet profil et ses attributs
        ville_depart : str
            La ville dont l'utilisateur souhaite rechercher son trajet 
        date : str
            La date à laquelle l'utilisateur souhaite rechercher son trajet
        """

        super().__init__()
        self.profil = profil
        self.ville_depart = ville_depart
        self.date=date

    def recherche(self):

        """Classe qui permet de rechercher les trajets parmi ceux disponibles sur la SNCF.

        Returns
        ----------
        result : Trajet
            Le ou les trajets disponibles en fonction des critères préalablement renseignés
        """
        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient= Trajetclient()
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets2(self.ville_depart,id_initial)
        trajetdao.insert_trajets(trajets)
        # on discutera est ce qu'on va stocker les résultats
        #for j in trajets :
        #    RechercheDAO().create(self.profil,j)
        #on a pas assez d'infos pour faire une select mais on va retourner directement trajets ou on dois ecrire une autre select
        #resultat_req =trajetdao.find_by_depart(self.trajet.date_depart, self.trajet.heure_depart, self.trajet.ville_depart, self.trajet.ville_arrivee)
        result=trajetdao.find_disponibilite(self.date,self.ville_depart)
        return result
    
    
    def sauvegarder(self):

        """Classe qui permet de sauvegarder les trajets trouvés par ce profil"""

        rechercheDAO.save(self.profil, self.trajet)

    def creer_alerte(self):

        """Classe qui permet de créer une alerte mail si un trajet correspondant aux critères est disponible"""

        rechercheDAO.creer_alerte(self.trajet, self.profil)
    
    
        


