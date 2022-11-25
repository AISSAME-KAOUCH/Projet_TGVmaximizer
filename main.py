from views.start_view import StartView
from client.trajet_client import Trajetclient
from business_object.trajet import Trajet
from DAO.trajetDAO import TrajetDAO
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.profil import Profil
from DAO.rechercheDAO import RechercheDAO 
from business_object.recherches.recherche_disponibilite import Recherche_disponibilite
from business_object.recherches.recherche_aller_retour import Recherche_aller_retour
if __name__ == '__main__':


    #run the StartView
    current_view = StartView()
    
    while current_view:
        
        print('-----------------')
        current_view.display_info()
        current_view = current_view.make_choice()

    
   

    