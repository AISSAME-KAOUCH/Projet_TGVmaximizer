from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.trajet import Trajet
from business_object.profil import Profil
class AllerRetourView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'ville_depart',
                'message': 'Quelle est la ville de depart ? (obligatoire)',
            },
            {
                'type': 'input',
                'name': 'ville_arrivee',
                'message': 'Quelle est la ville d\'arrivee ? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'date_depart',
                'message': 'Quelle est la date de depart ? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'date_arrivee',
                'message': 'Quelle est la date d\'arrivee pour le retour? (facultatif)',
            },
            {
                'type': 'input',
                'name': 'heure_depart',
                'message': 'Quelle est l\'heure de depart ? (facultatif)',
            },{
                'type': 'input',
                'name': 'heure_arrivee',
                'message': 'Quelle est l\'heure de depart pour le retour? (facultatif)',
            },{
                'type': 'input',
                'name': 'heure_arrivee_retour',
                'message': 'Quelle est l\'heure d\'arrivee pour le retour? (facultatif)',
            }  
        ]

    def display_info(self):
        print("Veuillez remplir les criteres de recherche.")

    def make_choice(self):

        reponses = prompt(self.__questions)
        ville_intramuros = ['PARIS','LYON','LILLE']

        from DAO.trajetDAO import TrajetDAO
        from client.trajet_client import Trajetclient
        from business_object.recherches.recherche_aller_retour import Recherche_aller_retour
        Session().trajet_aller = Trajet(id, ville_depart = reponses['ville_depart'].upper(),date_depart =reponses['date_depart'], heure_depart = reponses['heure_depart'], ville_arrivee = reponses['ville_arrivee'].upper() , heure_arrivee =reponses['heure_arrivee'],disponibilite_max='OUI')
        Session().trajet_retour = Trajet(id, ville_depart = reponses['ville_arrivee'].upper(),  date_depart =reponses['date_arrivee'], heure_depart = reponses['heure_arrivee'], ville_arrivee = reponses['ville_depart'].upper() , heure_arrivee =reponses['heure_arrivee_retour'],disponibilite_max='OUI')
        
        #cas où c'est paris lyon lille 
        if Session().trajet_aller.ville_depart in ville_intramuros : 
            Session().trajet_aller.ville_depart += ' (intramuros)'
        if Session().trajet_aller.ville_arrivee in ville_intramuros :
             Session().trajet_aller.ville_arrivee += ' (intramuros)'
        if Session().trajet_retour.ville_depart in ville_intramuros : 
            Session().trajet_retour.ville_depart += ' (intramuros)'
        if Session().trajet_retour.ville_arrivee in ville_intramuros :
             Session().trajet_retour.ville_arrivee += ' (intramuros)'
        
        profil = Profil(Session().profil._civilite,Session().profil._prenom,Session().profil._nom,Session().profil._date_de_naissance,Session().profil.email,Session().profil._mot_de_passe)
        (res1,res2) = Recherche_aller_retour(profil, Session().trajet_aller, Session().trajet_retour).recherche()
        
        if len(res1) == 0 :
            print('Pas de trajet aller corespondant à votre recherche')
        if len(res2) == 0 :
            print('Pas de trajet retour corespondant à votre recherche')
        
        for trj in res1 :
            print(trj.__str__())
        for trj in res2: 
            print(trj.__str())
        
        
        from views.menu_view import MenuView
        return MenuView()