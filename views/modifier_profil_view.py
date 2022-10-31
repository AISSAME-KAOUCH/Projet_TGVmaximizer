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
                    'Modifier mot de passe'
                    , 'Modifier addresse mail'
                    , 'Modifier prenom'
                    , 'Modifier nom'
                    , 'Retour menu'
                ]
            }
        ]


    def display_info(self):
        print('Veuillez choisir une action.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)

        if reponse['choice'] == 'retour menu':
            from views.menu_view import MenuView
            return MenuView()
        
        modifier = [{
                'type': 'input',
                'name': 'input',
                'message': 'Saisir'
            }]
        res = prompt(modifier)
        
        if reponse['choice'] == 'modifier mot de passe':
            profil_modifie = Session().profil
            profil_modifie._mot_de_passe = res['input']
            ProfilDAO().modifier_profil(profil_modifie)

            print(session().profil)

            from views.menu_view import MenuView
            return MenuView()

        elif reponse['choice'] == 'modifier addresse mail':
            #action a faire 
            from views.menu_view import MenuView
            return MenuView()

        elif reponse['choice'] == 'modifier prenom':
            #action a faire 
            from views.menu_view import MenuView
            return MenuView()

        elif reponse['choice'] == 'modifier nom':
            #action a faire 
            from views.menu_view import MenuView
            return MenuView()
        
