from PyInquirer import  prompt
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
                        'Recherche aller simple'
                        , 'Recherche aller retour'
                        , 'Recherche 30 jours'
                        , 'Retour menu'
                    ]
                }
            ]