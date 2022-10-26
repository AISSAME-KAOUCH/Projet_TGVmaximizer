from db_connection import DBConnection
from business_object.profil import Profil

class ProfilDAO(metaclass=Singleton):
    
    def find_by_id(self, email : str) -> Profil:

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

        request = "UPDATE profil" \
                  "SET mot_de_passe = '%(mdp)s'" \
                  "WHERE email = '%(email)s'"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : email, "mdp" : profil_modifie._mot_de_passe}
                )

    def modifier_profil(profil_modifie):

        request = "UPDATE profil" \
                  "SET nom = %(nom)s"\ 
                  ",prenom = %(prenom)s"\ 
                  ",civilite = %(civilite)s"\ 
                  ",date_de_naissance = %(date_de_naissance)s"\
                  ",email = %(email)s" \
                  "WHERE email = '%(email)s'"
          with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : profil_modifie.email, "nom" : profil_modifie.nom, "prenom" : profil_modifie.prenom, "civilite": profil_modifie.civilite, "date_de_naissance": profil_modifie.date_de_naissance}
                )
                res = cursor.fetchall() 
    
    def create_profil(profil):
        pass
    
