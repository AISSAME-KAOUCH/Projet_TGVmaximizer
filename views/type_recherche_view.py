from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session

class RechercheView(AbstractView):

    def __init__(self):
            self.__questions = [
                {
                    'type': 'list',
                    'name': 'choice',
                    'message': '',
                    'choices': [
                        'Recherche aller simple'
                        , 'Recherche aller retour'
                        , 'Recherche des departs à 30 jours'
                        , 'Retour menu'
                    ]
                }
            ]
    def display_info(self):
        print('Bonjour, veuillez choisir un type de trajet.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)
        
        if reponse['choice'] == 'Recherche aller simple':
            from views.aller_simple_view import AllerSimpleView
            return AllerSimpleView()
        elif reponse['choice'] == 'Recherche aller retour':
            from views.aller_retour_view import AllerRetourView
            return AllerRetourView()
        elif reponse['choice'] == 'Recherche des departs à 30 jours':
            from views.affichage_30j_view import Recherche30jView
            return Recherche30jView()
        elif reponse['choice'] == 'Retour menu':
            from views.menu_view import MenuView
            return MenuView()