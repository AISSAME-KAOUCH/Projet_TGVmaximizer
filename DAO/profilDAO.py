from DAO.db_connection import DBConnection
from business_object.profil import Profil
import requests
from utils.singleton import Singleton

class ProfilDAO(metaclass=Singleton):

    """Classe permettant la communication avec notre base de données en ce qui concerne les profils. 
    Elle permet de récupérer des profils depuis notre base de données mais aussi d'en ajouter
    et de les modifier. """

    def find_by_id(self, email : str) -> Profil:

        """Fonction permettant de récupérer, dans la base de données, le profil correspondant 
        à l'adresse mail donnée, et de stocker les informations de ce profil dans un objet Profil.

        Parameters
        ----------
        email : str
            email correspondant au profil que l'on souhaite importer
        ----------
        Returns
        ----------
        Profil : le profil associé à l'email recherché et contenant toutes les informations
        de l'utilisateur.

        """

        profil = None

        request = "SELECT * FROM profil " \
                  "WHERE email = %(email)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : email}
                )
                res = cursor.fetchone()
        if res:        
            profil = Profil(nom = res['nom'], 
                            prenom = res['prenom'], 
                            date_de_naissance = res['date_de_naissance'],
                            civilite = res['civilite'],
                            email = res['email'], 
                            mot_de_passe = res['mot_de_passe'])
        return profil

    def modifier_mot_de_passe(self, profil_modifie: Profil):

        """Fonction qui permet de modifier le mot de passe dans la base de données.
        
        Parameters
        ----------
        profil_modifie : Profil
            Profil de l'utilisateur qui contient ses informations et le nouveau mot de passe.

        Returns
        -------
        BOOL : True si la modification du mot de passe a bien été réalisée dans la base de données, 
        False sinon.
        """

        updated = False
        request = "UPDATE profil " \
                  "SET mot_de_passe = %(mdp)s" \
                  "WHERE email = %(email)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : profil_modifie.email, "mdp" : profil_modifie._mot_de_passe}
                )
                if cursor.rowcount :
                    updated = True
        return updated

    def modifier_profil(self, profil_modifie: Profil):

        """Fonction qui permet de modifier le profil dans la base de données.
        
        Parameters
        ----------
        profil_modifie : Profil
            Profil de l'utilisateur qui contient ses nouvelles informations.

        Returns
        -------
        BOOL : True si la modification du profil a bien été réalisée dans la base de données, 
        False sinon.
        """

        updated = False
        request = "UPDATE profil SET " \
                  "nom = %(nom)s ,prenom = %(prenom)s, civilite = %(civilite)s, date_de_naissance = %(date_de_naissance)s, email = %(email)s" \
                  "WHERE email = %(email)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : profil_modifie.email, "nom" : profil_modifie._nom, "prenom" : profil_modifie._prenom, "civilite": profil_modifie._civilite, "date_de_naissance": profil_modifie._date_de_naissance}
                )
                if cursor.rowcount :
                    updated = True
        return updated
    
    def create_profil(self, profil : Profil):

        """Fonction qui permet de stocker dans la base de données un nouveau profil à partir
        d'un objet métier Profil.
        
        Parameters
        ----------
        profil_modifie : Profil
            Profil que l'on souhaite stocker dans la base de données.

        Returns
        -------
        None
        """
        
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute('INSERT INTO profil (civilite, prenom, nom, date_de_naissance, email, mot_de_passe) '\
                    'VALUES (%(civilite)s, %(prenom)s, %(nom)s, %(date_de_naissance)s, %(email)s, %(mot_de_passe)s)'\
                        ,{"civilite" : profil._civilite
                        , "prenom" : profil._prenom
                        , "nom" : profil._nom
                        , "date_de_naissance" : profil._date_de_naissance
                        , "email": profil.email
                        , "mot_de_passe": profil._mot_de_passe})
                #res = cursor.fetchall()
