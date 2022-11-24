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

        modifier_civ = [{
                'type': 'input',
                'name': 'input',
                'message': 'Entrer la nouvelle donnée (format M ou MME) :'
            }]
        
        if reponse['choice'] == 'Modifier civilite':
            res = prompt(modifier_civ)
            if res['input'] == "M" or res['input'] == "MME" : 
                Session().profil.modifier_civilite(res['input'])
                ProfilDAO().modifier_profil(Session().profil)
                from views.menu_view import MenuView
                return MenuView()
            else:
                print("Format de la civilité incorrect")
                from views.modifier_profil_view import ModifierView
                return ModifierView()

        elif reponse['choice'] == 'Modifier prenom':
            res = prompt(modifier)
            Session().profil.modifier_prenom(res['input'])
            ProfilDAO().modifier_profil(Session().profil)
            from views.menu_view import MenuView
            return MenuView()

        elif reponse['choice'] == 'Modifier nom':
            res = prompt(modifier)
            Session().profil.modifier_nom(res['input'])
            ProfilDAO().modifier_profil(Session().profil)
            from views.menu_view import MenuView
            return MenuView()
        
        elif reponse['choice'] == 'Modifier mot de passe':
            #res = prompt(modifier)
            mdp = sha256(getpass.getpass(' Entrez le nouveau mot de passe : ').encode() + salt.encode()).hexdigest()
            Session().profil.modifier_mdp(mdp)
            ProfilDAO().modifier_mot_de_passe(Session().profil)
            from views.menu_view import MenuView
            return MenuView()
        
