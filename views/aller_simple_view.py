from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.trajet import Trajet
from business_object.profil import Profil
class AllerSimpleView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'ville_depart',
                'message': 'Quelle est la ville de depart ?',
            },
            {
                'type': 'input',
                'name': 'ville_arrivee',
                'message': 'Quelle est la ville d\'arrivee ?',
            },
            {
                'type': 'input',
                'name': 'date_depart',
                'message': 'Quel est la date de depart (Format JJ-MM-YYYY) ? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'heure_depart',
                'message': 'Quelle est l\'heure de depart ?',
            },{
                'type': 'input',
                'name': 'heure_arrivee',
                'message': 'Quelle est l\'heure d\'arrivee ? (facultatif)',
            }  
        ]

    def display_info(self):
        print("Veuillez remplir les criteres de recherche.")

    def make_choice(self):

        reponses = prompt(self.__questions)
        ville_intramuros = ['PARIS','LYON','LILLE']

        from DAO.trajetDAO import TrajetDAO
        from client.trajet_client import Trajetclient
        from business_object.recherches.recherche_aller import Recherche_aller
        Session().trajet = Trajet(id, ville_depart = reponses['ville_depart'].upper(),  date_depart =reponses['date_depart'], heure_depart = reponses['heure_depart'], ville_arrivee = reponses['ville_arrivee'].upper() , heure_arrivee =reponses['heure_arrivee'],disponibilite_max='OUI')
        if Session().trajet.ville_depart in ville_intramuros : 
            Session().trajet.ville_depart += ' (intramuros)'
        if Session().trajet.ville_arrivee in ville_intramuros :
             Session().trajet.ville_arrivee += ' (intramuros)'
        profil = Profil(Session().profil._civilite,Session().profil._prenom,Session().profil._nom,Session().profil._date_de_naissance,Session().profil.email,Session().profil._mot_de_passe)
        res =Recherche_aller(profil,Session().trajet).recherche()
        if len(res) == 0 : 
            print('Pas de trajet corespondant à votre recherche')
        for trj in res :
            print(trj.__str__())
        from views.menu_view import MenuView
        return MenuView()
        
        
        
