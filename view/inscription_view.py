from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session
from business_object.profil import Profil


class InscriptionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'prenom',
                'message': 'Quel est votre prenom?',
            },
            {
                'type': 'input',
                'name': 'nom',
                'message': 'Quel est votre nom?',
            },
            {
                'type': 'input',
                'name': 'date_naissance',
                'message': 'Quelle est votre date de naissance ? Saisir au format JJ/MM/AAAA',
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Quel est votre email?',
            },
            {
                'type': 'input',
                'name': 'mdp',
                'message': 'Choisir un mot de passe :',
            },
            {
                'type': 'input',
                'name': 'civilite',
                'message': 'Quel est votre sexe? Saisir au format H ou M',
            }

        ]

    def display_info(self):
        print("Veuillez remplir le formulaire.")

    def make_choice(self):

        answers = prompt(self.__questions)


        from DAO.profilDAO import ProfilDAO
        profil = ProfilDAO().find_by_id(answers['email'])
        if profil:
            print('L\'addresse mail est deja prise')
            from view.start_view import StartView
            return StartView()
        else:
            Session().profil = Profil(answers['nom'], answers['prenom'], answers['date_naissance'], answers['civilite'], answers['email'] , answers['mdp'])
            ProfilDAO().create_profil(Session().profil)
            from view.menu_view import MenuView
            return MenuView()
        
        
        
