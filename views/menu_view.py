from PyInquirer import Separator, prompt
from views.abstract_view import AbstractView
from views.session import Session

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
        print(f'Bonjour {Session().profil._prenom}, veuillez choisir une action.')

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

