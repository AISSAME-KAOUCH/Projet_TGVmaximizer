import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.profil import Profil
from business_object.trajet import Trajet

def creer_alerte(recherche, trajet):
    # on crée un e-mail
    message = MIMEMultipart("alternative")
    # on ajoute un sujet
    message["Subject"] = "[TGVMAXimizer] Nouveau trajet disponible"
    # un émetteur
    message["From"] = "tgvmaximizer@gmail.com"
    # un destinataire
    message["To"] = recherche.profil.email

    # on crée un texte et sa version HTML
    texte = "Bonjour,\n\n Vous avez récemment sauvegardé cette recherche sur notre application TGVMAXimizer: \n {} \n\n Nous avons le plaisir de vous informer qu'une place correspondante est disponible :\n {} \n\n Bonne journée et bon voyage !".format(recherche.trajet.__str__(), trajet.__str__())

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
        server.sendmail("tgvmaximizer@gmail.com", recherche.profil.email, message.as_string())