from PyInquirer import prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.profil import Profil
from hashlib import sha256
import getpass

class InscriptionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'civilite',
                'message': 'Quel est votre sexe ? Saisir au format H ou F',
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
        #     {
        #         'type': 'input',
        #         'name': 'mdp',
        #         'message': sha512(getpass.getpass('Quel est votre mot de passe ?').encode()).hexdigest(),
        #     },
        ]

    def display_info(self):
        print("Veuillez remplir le formulaire d'inscription.")

    def make_choice(self):

        reponses = prompt(self.__questions)
        salt = reponses['email']
        mdp = sha256(getpass.getpass('? Quel est votre mot de passe ?').encode() + salt.encode()).hexdigest()
        
        from DAO.profilDAO import ProfilDAO
        profil = ProfilDAO().find_by_id(reponses['email'])
        if profil:
            print('L\'addresse email est deja prise')
            from views.start_view import StartView
            return StartView()
        else:
            #mdp = mdp.encode()
            #mdp_sign = sha256(mdp + salt.encode()).hexdigest()
            Session().profil = Profil(reponses['civilite'], reponses['prenom'], reponses['nom'], reponses['date_naissance'], reponses['email'] , mdp)
            ProfilDAO().create_profil(Session().profil)
            print('Le compte est cree avec succes')
            from views.start_view import StartView
            return StartView()
        
        
        
