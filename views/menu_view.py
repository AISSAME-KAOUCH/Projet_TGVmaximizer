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
                    'Recherche de trajet(s)'
                    , 'Modifier mon profil'
                    , 'Deconnexion'
                ]
            }
        ]

    def display_info(self):
        print(f'Bonjour {Session().profil._civilite}. {Session().profil._prenom} {Session().profil._nom}, veuillez choisir une action.')

    def make_choice(self):
        
        reponses = prompt(self.__questions)
        
        if reponses['choice'] == 'Recherche de trajet(s)':
            from views.type_recherche_view import RechercheView
            return RechercheView()
        if reponses['choice'] == 'Modifier mon profil':
            from views.modifier_profil_view import ModifierView
            return ModifierView()
        elif reponses['choice'] == 'Deconnexion':
            from views.start_view import StartView
            return StartView()
