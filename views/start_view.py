from PyInquirer import Separator, prompt
from views.abstract_view import AbstractView
from views.session import Session

class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': '',
                'choices': [
                    'Connexion'
                    , 'Inscription'
                    , 'Quitter'
                ]
            }
        ]

    def display_info(self):
        print('Bonjour, veuillez choisir une action.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)
        
        if reponse['choice'] == 'Connexion':
            from views.connexion_view import ConnexionView
            return ConnexionView()
        elif reponse['choice'] == 'Inscription':
            from views.inscription_view import InscriptionView
            return InscriptionView()
        elif reponse['choice'] == 'Quitter':
            return None

        
        
