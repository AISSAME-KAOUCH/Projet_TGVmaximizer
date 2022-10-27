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
                    'modifier mot de passe'
                    , 'modifier addresse mail'
                    , 'modifier prenom'
                    , 'modifier nom'
                    , 'retour menu'
                ]
            },{
                    'type': 'input',
                    'name': 'input',
                    'message': 'Saisir :',
                }
        ]



    

    def display_info(self):
        print(f'Veuillez choisir une action {Session().profil._prenom}.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)
        
        if reponse['choice'] == 'modifier mot de passe':
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'modifier addresse mail':
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'modifier prenom':
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'modifier nom':
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'retour menu':
            from view.menu_view import MenuView
            return MenuView()

        
        