import datetime as dt

class Profil : 

    """ Profil contenant les informations de l'utilisateur et donc qui le représente
        numériquement dans l'application.
    """

    def __init__(self, civilite, prenom, nom, date_de_naissance, email, mot_de_passe):
        """ Constructeur permettant l'instanciation d'un objet Profil.

        Parameters
        ----------
        civilite : str
            civilite de l'utilisateur
        prenom : str
            prénom de l'utilisateur
        nom : str
            nom de famille de l'utilisateur
        date_de_naissance : str
            date de naissance de l'utilisateur
        email : str 
            adresse mail de l'utilisateur
        mot de passe : str
            mot de passe de l'utilisateur
        """
        self._civilite = civilite
        self._prenom = prenom
        self._nom = nom 
        self._date_de_naissance = date_de_naissance
        self.email = email
        self._mot_de_passe = mot_de_passe

    def modifier_mdp(self, new_pass):
        """ Fonction permettant de modifier le mot de passe de l'utilisateur

        Parameters
        ----------
        new_pass : str
            nouveau mot de passe

        Returns
        -------
            None
        """
        self._mot_de_passe = new_pass
    
    def modifier_nom(self, nom):
        """ Fonction permettant de modifier le nom de l'utilisateur

        Parameters
        ----------
        nom : str
            nouveau nom

        Returns
        -------
            None
        """
        self._nom = nom
    
    def modifier_prenom(self, prenom):
        """ Fonction permettant de modifier le prénom de l'utilisateur

        Parameters
        ----------
        prenom : str
            nouveau prenom

        Returns
        -------
            None
        """
        self._prenom = prenom

    def modifier_civilite(self, civilite):
        """ Fonction permettant de modifier la civilité de l'utilisateur

        Parameters
        ----------
        civilite : str
            nouvelle civilité

        Returns
        -------
            None
        """
        self._civilite = civilite
    
    def modifier_date_de_naissance(self, date):
        """ Fonction permettant de modifier la date de naissance de l'utilisateur

        Parameters
        ----------
        date : str
            nouvelle date de naissance

        Returns
        -------
            None
        """
        self._date_de_naissance = date
    
    def modifier_email(self, mail):
        """ Fonction permettant de modifier l'adresse mail de l'utilisateur

        Parameters
        ----------
        mail : str
            nouvelle adresse mail

        Returns
        -------
            None
        """
        self.email = mail
    
    def modifier_profil(self):
        """ Fonction permettant de modifier un ou plusieurs élément du profil de l'utilisateur.
        Cette fonction fait appel aux precédentes fonctions de modification.

        Parameters
        ----------

        Returns
        -------
            None
        """
        choix  = 0 
        while choix < 1 or choix > 6 :
            choix = int(input(' 1. Modifier le mot de passe \n'
            '2. Modifier le nom \n'
            '3. Modifier le prenom \n'
            '4. Modifier la civilité \n'
            '5. Modifier la date de naissance \n'
            '6. Modifier l\'adresse mail \n'
            'Taper le numéro correspondant :'))
            actions = {1:self.modifier_mdp,
                       2:self.modifier_nom,
                       3:self.modifier_prenom,
                       4:self.modifier_civilite,
                       5:self.modifier_date_de_naissance,
                       6:self.modifier_email}
            action = actions.get(choix)
            action(input("entrer la nouvelle valeur :"))
        

    def type_abonnement(self):
        """ Fonction permettant d'identifier le type d'abonnement de l'utilisateur à partir
        de sa date de naissance.

        Parameters
        ----------

        Returns
        -------
        str : type d'abonnement = {'jeune', 'senior', 'pas éligible'}
        """
        self._date_de_naissance = dt.datetime.strptime(self._date_de_naissance,'%d-%m-%Y').date()
        age = (dt.date.today() - self._date_de_naissance).days
        if age > 5840 and age < 9855 : # = ou >= ?
            res = 'jeune'
        elif age > 21900 :
            res = 'senior'
        else : 
            res = 'pas éligible'
        return res 

    def __str__(self): 
        """ Fonction permettant d'afficher les information du profil (toutes sauf le mot de passe)

        Parameters
        ----------

        Returns
        -------
        str : les informations du profil 
        """
        return 'Profil de {}. {} {} :\n Email: {} \n Date de naissance : {} '.format(self._civilite,self._nom, self._prenom,self.email,self._date_de_naissance)  


