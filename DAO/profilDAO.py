from db_connection import DBConnection
from business_object.profil import Profil

class ProfilDAO(metaclass=Singleton):
    
    def create(self, email : str) -> Profil:

        request = "SELECT * FROM profil" \
                  "WHERE email = %(email)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : email}
                )
                res = cursor.fetchall()
        profil = Profil(nom = res['nom'], 
                        prenom = res['prenom'], 
                        date_de_naissance = res['date_de_naissance'],
                        civilite = res['civilite'],
                        email = res['email'], 
                        mot_de_passe = res['mot_de_passe'])
        return profil

    def modifier_mot_de_passe(profil_modifie):
        mdp = profil_modifie._mot_de_passe
        email = profil_modifie.email
        request = "UPDATE profil" \
                  "SET mot_de_passe = '%(mdp)s'" \
                  "WHERE email = '%(email)s'" 

    def modifier_profil(profil_modifie):
        nom = profil_modifie._nom
        prenom = profil_modifie._prenom
        email = profil_modifie.email 
        civilite = profil_modifie._civilite
        date_de_naissance = profil_modifie._date_de_naissance
        request = "UPDATE profil" \
                  "SET nom = %(nom)s,"\ 
                  "prenom = %(prenom)s"\ 
                  ",civilite = %(civilite)s,\ 
                  "date_de_naissance = %(date_de_naissance)s"\
                  ",email = %(email)s" \
                  "WHERE email = '%(email)s'" 
    