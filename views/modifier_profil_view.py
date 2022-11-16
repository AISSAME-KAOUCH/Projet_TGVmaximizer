from PyInquirer import Separator, prompt
from views.abstract_view import AbstractView
from views.session import Session
from DAO.profilDAO import ProfilDAO

class ModifierView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choice',
                'message': '',
                'choices': [
                    'Modifier civilite'
                    , 'Modifier prenom'
                    , 'Modifier nom'
                    , 'Modifier mot de passe'
                    , 'Retour menu'
                ]
            }
        ]


    def display_info(self):
        print('Veuillez choisir une action.')
        

    def make_choice(self):
        
        reponse = prompt(self.__questions)

        if reponse['choice'] == 'Retour menu':
            from views.menu_view import MenuView
            return MenuView()
        
        modifier = [{
                'type': 'input',
                'name': 'input',
                'message': 'Entrer la nouvelle donnée :'
            }]

        res = prompt(modifier)
        
        if reponse['choice'] == 'Modifier civilite':
            Session().profil.modifier_civilite(res['input'])
            ProfilDAO().modifier_profil(Session().profil)
            from views.menu_view import MenuView
            return MenuView()

        elif reponse['choice'] == 'Modifier prenom':
            Session().profil.modifier_prenom(res['input'])
            ProfilDAO().modifier_profil(Session().profil)
            from views.menu_view import MenuView
            return MenuView()

        elif reponse['choice'] == 'Modifier nom':
            Session().profil.modifier_nom(res['input'])
            ProfilDAO().modifier_profil(Session().profil)
            from views.menu_view import MenuView
            return MenuView()
        
        elif reponse['choice'] == 'Modifier mot de passe':
            Session().profil.modifier_mdp(res['input'])
            ProfilDAO().modifier_mot_de_passe(Session().profil)
            from views.menu_view import MenuView
            return MenuView()
        
