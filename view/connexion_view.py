from pprint import pprint

from PyInquirer import  prompt
from view.abstract_view import AbstractView
from view.session import Session



class   ConnexionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'email',
                'message': 'Quel est votre identifiant ? (email)'
            },{
                'type': 'input',
                'name': 'mdp',
                'message': 'Quel est votre mot de passe ? '
            }
        ]

    def display_info(self):
        print("Veuillez entrer les informations requisent a la connexion.")

    def make_choice(self):
        
        answers = prompt(self.__questions)


        from business_object.profil import Profil
        profil = Profil.charger(answers['email'], answers['mdp'])

        if profil:
            Session().profil = profil
            from view.menu_view import MenuView
            return MenuView()
        else:
            print('Identifiant / mot de passe non reconnu.')
            from view.start_view import StartView
            return StartView()