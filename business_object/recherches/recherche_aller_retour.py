from business_object.recherches.abstract_recherche import AbstractRecherche
from DAO.rechercheDAO import RechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient
from business_object.profil import Profil

class Recherche_aller_retour(AbstractRecherche):

    def __init__(self, profil: Profil, trajet_aller: Trajet, trajet_retour: Trajet) -> None:
        super().__init__()
        self.trajet_aller = trajet_aller
        self.trajet_retour = trajet_retour
        self.profil = profil

    def recherche(self):
        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient = Trajetclient()
        jour = self.trajet_aller.date_depart[:2] # On tire les informations
        mois = self.trajet_aller.date_depart[3:5]# dont on a besoin 
        annee = self.trajet_aller.date_depart[6:10] # de l'attribut date_depart
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets(annee, mois, jour, self.trajet_aller.ville_depart, self.trajet_aller.ville_arrivee,id_initial)
        trajetdao.insert_trajets(trajets)
        for j in trajets :
            RechercheDAO().create(self.profil,j)
        resultat_req1 =trajetdao.find_by_depart(self.trajet_aller.date_depart, self.trajet_aller.heure_depart, self.trajet_aller.ville_depart, self.trajet_aller.ville_arrivee)

        jour_retour = self.trajet_retour.date_depart[:2] # On tire les informations
        mois_retour = self.trajet_retour.date_depart[3:5]# dont on a besoin 
        annee_retour = self.trajet_retour.date_depart[6:10] # de l'attribut date_depart
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets(annee_retour, mois_retour, jour_retour, self.trajet_retour.ville_depart, self.trajet_retour.ville_arrivee,id_initial)
        trajetdao.insert_trajets(trajets)
        for j in trajets :
            RechercheDAO().create(self.profil,j)
        resultat_req2 =trajetdao.find_by_depart(self.trajet_retour.date_depart, self.trajet_retour.heure_depart, self.trajet_retour.ville_depart, self.trajet_retour.ville_arrivee)
               
        # Affichage intégré         
        return (resultat_req1,resultat_req2)
    
    def sauvegarder(self):
        rechercheDAO.sauvegarder(self.trajet, self.profil)
    
    def creer_alerte(self):
            # on crée un e-mail
            message = MIMEMultipart("alternative")
            # on ajoute un sujet
            message["Subject"] = "[TGVMAXimizer] Nouveau trajet disponible"
            # un émetteur
            message["From"] = "tgvmaximizer@gmail.com"
            # un destinataire
            message["To"] = self.recherche.profil.email

            # on crée un texte et sa version HTML
            texte = "Bonjour,\n\n Vous avez récemment sauvegardé cette recherche sur notre application TGVMAXimizer: \n {} \n\n Nous avons le plaisir de vous informer qu'une place correspondante est disponible :\n {} \n\n Bonne journée et bon voyage !".format(self.recherche.trajet.__str__(), self.trajet.__str__())

            # on crée un élément MIMEText 
            texte_mime = MIMEText(texte, 'plain')

            # on attache cet élément 
            message.attach(texte_mime)

            # on crée la connexion
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # connexion au compte
                server.login("tgvmaximizer@gmail.com", "gfhd witr sapg frih")
                # envoi du mail
                server.sendmail("tgvmaximizer@gmail.com", self.recherche.profil.email, message.as_string())
    
        


