from pprint import pprint
from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session

class StartView(AbstractView):

    def __init__(self):
            self.__questions = [
                {
                    'type': 'list',
                    'name': 'choice',
                    'message': '',
                    'choices': [
                        'Aller simple'
                        , 'Aller retour'
                        , 'Quitter'
                    ]
                }
            ]