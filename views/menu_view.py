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
                    'Filtre de recherche'
                    , 'Modifier son profil'
                    , 'Quitter'
                ]
            }
        ]

    def display_info(self):
        print(f'Veuillez choisir une action {Session().profil._prenom}.')

    def make_choice(self):
        
        reponses = prompt(self.__questions)
        
        if reponses['choice'] == 'Filtre de recherche':
            from view.filtre_view import FiltreView
            return FiltreView()
        if reponses['choice'] == 'Modifier son profil':
            from view.modifier_profil_view import ModifierView
            return ModifierView()
        elif reponses['choice'] == 'Quitter':
            return None

