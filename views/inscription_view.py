from PyInquirer import prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.profil import Profil
from hashlib import sha256
import getpass
import re
from utils.fonctions_diverses import type_abonnement_general


class InscriptionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'civilite',
                'message': 'Quel est votre sexe ? Saisir au format M ou MME',
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
                'message': 'Quelle est votre date de naissance ? Saisir au format JJ-MM-AAAA',
            },
            {
                'type': 'input',
                'name': 'email',
                'message': 'Quel est votre email ?',
            }
        ]

    def display_info(self):
        print("Veuillez remplir le formulaire d'inscription.")

    def make_choice(self):

        reponses = prompt(self.__questions)
        salt = reponses['email']
        mdp = sha256(getpass.getpass('? Quel est votre mot de passe ?').encode() + salt.encode()).hexdigest()
        

        regex_date = r'\b^(?:(?:31(\-)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\-)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\-)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$\b'
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if reponses["civilite"] == "M" or reponses["civilite"] == "MME" : 
            if re.match(regex_date, reponses["date_naissance"]) : 
                if type_abonnement_general(reponses["date_naissance"]) == True :
                    if(re.fullmatch(regex_email, reponses['email'])) :
                        from DAO.profilDAO import ProfilDAO
                        profil = ProfilDAO().find_by_id(reponses['email'])
                        if profil:
                            print('L\'addresse email est deja prise')
                            from views.start_view import StartView
                            return StartView()
                        else:
                            Session().profil = Profil(reponses['civilite'], reponses['prenom'], reponses['nom'], reponses['date_naissance'], reponses['email'] , mdp)
                            ProfilDAO().create_profil(Session().profil)
                            print('Le compte est cree avec succes')
                            from views.start_view import StartView
                            return StartView()
                    else : 
                        print("Adresse mail incorrecte")
                else:
                    print("Vous n'êtes pas éligibles à TGVMax" )              
            else : 
                print("Format de la date incorrect")
        else:
            print("Format de la civilité incorrect")
        from views.inscription_view import InscriptionView
        return InscriptionView()    
        
        
        
