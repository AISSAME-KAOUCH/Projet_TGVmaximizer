from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session




class MenuView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': '',
                'choices': [
                    'faire ci'
                    , 'faire la'
                    , 'Quitter'
                ]
            }
        ]

    def display_info(self):
        print(f'Veuillez choisir une action {Session().profil._prenom}.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)
        
        if reponse['choice'] == 'faire ci':
            return self
        elif reponse['choice'] == 'faire la':
            return self
        elif reponse['choice'] == 'Quitter':
            return None

        
        
