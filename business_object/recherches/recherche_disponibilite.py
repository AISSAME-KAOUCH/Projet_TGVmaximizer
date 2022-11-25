from business_object.recherches.abstract_recherche import AbstractRecherche
from DAO.rechercheDAO import RechercheDAO 
from DAO.trajetDAO import TrajetDAO
from business_object.trajet import Trajet
from client.trajet_client import Trajetclient
from business_object.profil import Profil

class Recherche_disponibilite(AbstractRecherche):

    """Classe qui permet de rechercher dans la base de données les trajets demandés"""

    def __init__(self, profil, ville_depart, date):

        """Constructeur permettant l'instanciation d'une recherche pour un profil renseigné

        Parameters
        ---------- 
        profil : Profil 
            Un objet profil et ses attributs
        ville_depart : str
            La ville dont l'utilisateur souhaite rechercher son trajet 
        date : str
            La date à laquelle l'utilisateur souhaite rechercher son trajet
        """

        super().__init__()
        self.profil = profil
        self.ville_depart = ville_depart
        self.date=date

    def recherche(self):

        """Classe qui permet de rechercher les trajets parmi ceux disponibles sur la SNCF.

        Returns
        ----------
        result : Trajet
            Le ou les trajets disponibles en fonction des critères préalablement renseignés
        """
        trajetdao = TrajetDAO() # On instancie les classes de la couche DAO
        trajetclient = Trajetclient()
        id_initial = trajetdao.find_max_id() # On cherche l'identifiant de la dernière ligne de notre base de données
        trajets = trajetclient.get_trajets2(self.ville_depart,id_initial)
        trajetdao.insert_trajets(trajets)
        result = trajetdao.find_disponibilite(self.date,self.ville_depart)
        return result
    
    

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
    
    
        


