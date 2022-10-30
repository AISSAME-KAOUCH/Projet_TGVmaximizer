from pprint import pprint
from PyInquirer import prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.profil import Profil

class InscriptionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'civilite',
                'message': 'Quel est votre sexe ? Saisir au format H ou M',
            },
            {
                'type': 'input',
                'name': 'prenom',
                'message': 'Quel est votre prenom ?',
            },
            {
                'type': 'input',
                'name': 'nom',
                'message': 'Quel est votre nom ?',
            },
            {
                'type': 'input',
                'name': 'date_naissance',
                'message': 'Quelle est votre date de naissance ? Saisir au format JJ/MM/AAAA',
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Quel est votre email ?',
            },
            {
                'type': 'input',
                'name': 'mdp',
                'message': 'Choisir un mot de passe :',
            },
        ]

    def display_info(self):
        print("Veuillez remplir le formulaire d'inscription.")

    def make_choice(self):

        reponses = prompt(self.__questions)

        from DAO.profilDAO import ProfilDAO
        profil = ProfilDAO().find_by_id(reponses['email'])
        if profil:
            print('L\'addresse email est deja prise')
            from view.start_view import StartView
            return StartView()
        else:
            Session().profil = Profil(reponses['civilite'],  reponses['prenom'], reponses['nom'], reponses['date_naissance'], reponses['email'] , reponses['mdp'])
            ProfilDAO().create_profil(Session().profil)
            from view.menu_view import MenuView
            return MenuView()
        
        
        
