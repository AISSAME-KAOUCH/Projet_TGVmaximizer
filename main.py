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
    resultat=trajet.get_trajets('2022','11','02',"NANTES","LE+MANS")
    for tj in resultat :
        print(tj.__str__())

    test=TrajetDAO()
    test.insert_trajets(resultat)
