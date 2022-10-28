#from view.start_view import StartView
from client.trajet_client import Trajetclient
from business_object.trajet import Trajet
from DAO.trajetDAO import TrajetDAO
"""
if __name__ == '__main__':
    # run the StartView
    current_view = StartView()

    while current_view:
        
        print('-----------------')
        current_view.display_info()
        current_view = current_view.make_choice()
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
    

    
