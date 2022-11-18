from views.start_view import StartView
from client.trajet_client import Trajetclient
from business_object.trajet import Trajet
from DAO.trajetDAO import TrajetDAO
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.profil import Profil
if __name__ == '__main__':

    
    # run the StartView
    current_view = StartView()

    while current_view:
        
        print('-----------------')
        current_view.display_info()
        current_view = current_view.make_choice()

    '''
    profil=Profil('H', 'ali', 'ali', '15/10/2000', 'ali@gmail.com', '0000')
    trajet=Trajet(0,'RENNES','02-12-2022','11:51:00','LAVAL','12:48',5280,'OUI')
    res=Recherche_aller(profil,trajet).recherche()
    for trj in res :
        print(trj.__str__())
    '''
#PAS DE TEST DANS LE MAIN
"""
if __name__=='__main__' :
    trajet=Trajetclient()
    test=TrajetDAO()
    id_ini=test.find_max_id()
    print(id_ini[0]['maximum'])
    
    resultat=trajet.get_trajets('2022','11','08',"NANTES","LE+MANS",id_ini[0]['maximum'])
    #for tj in resultat :
    #    print(tj.__str__())

    
    test.insert_trajets(resultat)
    res=test.find_by_depart('2022-11-08','11:05','NANTES','LE MANS')
    #print(res)

   
    for t in res :
        print(t.__str__())      
    #for i in res :
    #    print(i.__str__())
"""    

    