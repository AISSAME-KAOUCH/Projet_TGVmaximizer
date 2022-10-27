from DAO.db_connection import DBConnection
from business_object.profil import Profil
import requests
from utils.singleton import Singleton

class ProfilDAO(metaclass=Singleton):

    """Permet d'ajouter à notre base de données les profils des utilisateurs """

    def find_by_id(self, email : str) -> Profil:

        """Trouver le profil qui correspond au mail qui est donné 

        Parameters
        ----------
        email : str
            email de l'utilisateur
        ----------
        Returns
        ----------
        profil : list
            Le profil associé à l'email de l'utilisateur avec la liste de ses informations

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

    def modifier_mot_de_passe(self,profil_modifie : Profil):

        """Fonction pour modifier le mot de passe dans la DB
        
        Parameters
        ----------
        profil_modifie : list
            La liste des éléments d'un profil avec le mot de passe modifié

        """

        request = "UPDATE profil" \
                  "SET mot_de_passe = '%(mdp)s'" \
                  "WHERE email = '%(email)s'"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : profil_modifie.email, "mdp" : profil_modifie._mot_de_passe}
                )

    def modifier_profil(self,profil_modifie):

        """Fonction pour modifier le profil dans la DB
        
        Parameters
        ----------
        profil_modifie : list
            La liste des éléments d'un profil dont les éléments à modifier
        """

        request = "UPDATE profil SET" \
                  "nom = %(nom)s ,prenom = %(prenom)s, civilite = %(civilite)s, date_de_naissance = %(date_de_naissance)s, email = %(email)s" \
                  "WHERE email = '%(email)s'"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute( 
                    request, {"email" : profil_modifie.email, "nom" : profil_modifie.nom, "prenom" : profil_modifie.prenom, "civilite": profil_modifie.civilite, "date_de_naissance": profil_modifie.date_de_naissance}
                )
    
    def create_profil(self,profil : Profil):
        with DBConnection().connection as connection :
            with connection.cursor() as cursor :
                cursor.execute('INSERT INTO profil (email,nom,prenom,mot_de_passe,civilite,date_de_naissance) '\
                    'VALUES (%(email)s, %(nom)s,%(prenom)s,%(mot_de_passe)s,%(civilite)s,%(date_de_naissance)s)'\
                        ,{"email": profil.email
                        , "nom" : profil._nom
                        , "prenom" : profil._prenom
                        , "mot_de_passe": profil._mot_de_passe
                        , "civilite" : profil._civilite
                        , "date_de_naissance" : profil._date_de_naissance})
                #res = cursor.fetchall()
