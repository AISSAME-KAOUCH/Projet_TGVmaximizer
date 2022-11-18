from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session
from hashlib import sha256
import getpass

class   ConnexionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'email',
                'message': 'Quel est votre identifiant ? (email)'
            },
        ]

    def display_info(self):
        print("Veuillez entrer les informations requisent a la connexion.")

    def make_choice(self):
        
        reponses = prompt(self.__questions)
<<<<<<< HEAD
        salt = reponses['email']
        mdp = sha256(getpass.getpass('Quel est votre mot de passe ?').encode() + salt.encode()).hexdigest()
=======
        mdp = sha512(getpass.getpass('? Quel est votre mot de passe ?').encode()).hexdigest()
>>>>>>> a7fb896702a881a47f8c2d34cf02f8612c47cdb6

        from DAO.profilDAO import ProfilDAO
        profil = ProfilDAO().find_by_id(reponses['email'])
        if profil:
            if profil._mot_de_passe == mdp:
                Session().profil = profil
                from views.menu_view import MenuView
                return MenuView()
        
        print('Identifiant / mot de passe non reconnu.')
        from views.start_view import StartView
        return StartView()