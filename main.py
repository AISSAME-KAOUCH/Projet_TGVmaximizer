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

    




    #profil=Profil('H', 'ali', 'ali', '15/10/2000', 'aissame@gmail.com', '0000')
    #trajet=Trajet(1,'RENNES','02-12-2022','11:51:00','LAVAL','12:48',67,'OUI')
    #trajet2=Trajet(1,'LAVAL','10-12-2022','07:40:00','RENNES','12:48',8,'OUI')
    #
    #(resultat_req1,resultat_req2)=Recherche_aller_retour(profil,trajet,trajet2).recherche()
    #print(len(resultat_req1),len(resultat_req2))
    #print('\n\n\t\t--------------aller---------------\n\n')
    #for i in resultat_req1 :
     #   print(i.__str__())
    #print('--------------retour---------------\n\n')
    #for j in resultat_req2 : 
     #   print(j.__str__())      
        


    #res=Recherche_30j(profil,'RENNES','02-12-2022').recherche()
    #for trj in res :
    #    print(trj.__str__())  
#PAS DE TEST DANS LE MAIN

#if __name__=='__main__' :
#    trajet=Trajetclient()
 #   test=TrajetDAO()
  #  id_ini=test.find_max_id()
   # print(id_ini[0]['maximum'])
    
    #resultat=trajet.get_trajets('2022','11','08',"NANTES","LE+MANS",id_ini[0]['maximum'])
    #for tj in resultat :
    #    print(tj.__str__())

    
    #test.insert_trajets(resultat)
    #res=test.find_by_depart('2022-11-08','11:05','NANTES','LE MANS')
    #print(res)

   
    #for t in res :
     #   print(t.__str__())      
    #for i in res :
    #    print(i.__str__())
#"""    

    