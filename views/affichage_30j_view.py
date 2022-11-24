from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.trajet import Trajet
from business_object.profil import Profil

class Recherche30jView(AbstractView):
    def __init__(self) -> None: 
        self.__questions = [
            {
                'type': 'input',
                'name': 'ville_depart',
                'message': 'Quelle est la ville de depart ? (obligatoire)' ,
            },
            {
                'type': 'input',
                'name': 'date_depart',
                'message': 'Quelle est la date de depart ? (obligatoire)' ,
            },
        ]
    def display_info(self):
        print("Veuillez remplir les criteres de recherche.")

    def make_choice(self):

        reponses = prompt(self.__questions)

        ville_intramuros = ['PARIS','LYON','LILLE']
        from DAO.trajetDAO import TrajetDAO
        from client.trajet_client import Trajetclient
        from business_object.recherches.recherche_30j import Recherche_30j

        if reponses['ville_depart'] in ville_intramuros :
            reponses['ville_depart'] += ' (intramuros)'
        
        profil = Profil(Session().profil._civilite,Session().profil._prenom,Session().profil._nom,Session().profil._date_de_naissance,Session().profil.email,Session().profil._mot_de_passe)
        res = Recherche_30j(profil,reponses['ville_depart'],reponses['date_depart']).recherche(self)
        if len(res) == 0 : 
            print('Pas de trajet corespondant à votre recherche')
        for trj in res :
            print(trj.__str__())
        from views.menu_view import MenuView
        return MenuView()
        

