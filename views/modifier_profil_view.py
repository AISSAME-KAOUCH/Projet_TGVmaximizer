from PyInquirer import Separator, prompt
from views.abstract_view import AbstractView
from views.session import Session

class ModifierView(AbstractView):

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
            }
        ]


    def display_info(self):
        print('Veuillez choisir une action.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)

        if reponse['choice'] == 'retour menu':
            from view.menu_view import MenuView
            return MenuView()
        
        modifier = [{
                'type': 'input',
                'name': 'input',
                'message': 'Saisir'
            }]
        res = prompt(modifier)
        
        if reponse['choice'] == 'modifier mot de passe': 
            #action a faire         session().profil.mdp
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'modifier addresse mail':
            #action a faire 
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'modifier prenom':
            #action a faire 
            from view.menu_view import MenuView
            return MenuView()
        elif reponse['choice'] == 'modifier nom':
            #action a faire 
            from view.menu_view import MenuView
            return MenuView()
        
