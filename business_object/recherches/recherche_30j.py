from business_object.recherches.abstract_recherche import AbstractRecherche
from DAO.rechercheDAO import RechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient
from business_object.profil import Profil

class Recherche_30j(AbstractRecherche):

    def __init__(self, profil, ville_depart, date):
        super().__init__()
        self.profil = profil
        self.ville_depart = ville_depart
        self.date=date

    def recherche(self):
        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient = Trajetclient()
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets2(self.ville_depart,id_initial)
        trajetdao.insert_trajets(trajets)
        # on discutera est ce qu'on va stocker les résultats
        #for j in trajets :
        #    RechercheDAO().create(self.profil,j)
        #on a pas assez d'infos pour faire une select mais on va retourner directement trajets ou on dois ecrire une autre select
        #resultat_req =trajetdao.find_by_depart(self.trajet.date_depart, self.trajet.heure_depart, self.trajet.ville_depart, self.trajet.ville_arrivee)
        result=trajetdao.find_disponibilite(self.date,self.ville_depart)
        return result
    
    
    def sauvegarder(self):
        rechercheDAO.save(self.profil, self.trajet)

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
    
    
        


