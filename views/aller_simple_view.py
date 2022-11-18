from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.trajet import Trajet
class AllerSimpleView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'ville_depart',
                'message': 'Quelle est la ville de depart ?',
            },
            {
                'type': 'input',
                'name': 'ville_arrivee',
                'message': 'Quelle est la ville d\'arrivee ? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'date_depart',
                'message': 'Quel est la date de depart ? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'date_arrivee',
                'message': 'Quelle est la date d\'arrivee ? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'heure_depart',
                'message': 'Quelle est l\'heure de depart ? (facultatif)',
            },{
                'type': 'input',
                'name': 'heure_arrivee',
                'message': 'Quelle est l\'heure d\'arrivee ? (facultatif)',
            }  
        ]

    def display_info(self):
        print("Veuillez remplir les criteres de recherche.")

    def make_choice(self):

        reponses = prompt(self.__questions)
        
        from DAO.trajetDAO import TrajetDAO
        from client.trajet_client import Trajetclient
        from business_object.recherches.recherche_aller import Recherche_aller
        Session().trajet = Trajet(id, reponses['ville_depart'],  reponses['date_depart'], reponses['heure_depart'], reponses['ville_arrivee'], reponses['date_arrivee'] , reponses['heure_arrivee'],'OUI')
        trajet=Trajetclient()
        Recherche_aller().recherche()
        #trajets=trajet.get_trajets(Session().trajet)
        #TrajetDAO().insert_trajets(trajets)
        ##
        from views.menu_view import MenuView
        return MenuView()
        
        
        
