import datetime as dt

class Profil : 

    """ Profil contenant les informations de l'utilisateur et donc qui le représente
        numériquement dans l'application.
    """

    def __init__(self, nom, prenom, date_de_naissance, civilite, email, mot_de_passe):
        """ Constructeur permettant l'instanciation d'un objet Profil.

        Parameters
        ----------
        nom : str
            nom de famille de l'utilisateur
        prenom : str
            prénom de l'utilisateur
        date_de_naissance : str
            date de naissance de l'utilisateur
        civilite : str
            civilite de l'utilisateur
        email : str 
            adresse mail de l'utilisateur
        mot de passe : str
            mot de passe de l'utilisateur
        """
        self._nom = nom 
        self._prenom = prenom
        self._date_de_naissance = date_de_naissance
        self._civilite = civilite
        self.email = email
        self._mot_de_passe = mot_de_passe

    def modifier_mdp(self):
        new_pass = input('Entrer nouveau mot de passe : ')
        self._mot_de_passe = new_pass
        print('Mot de passe modifié avec succès.')
    
    def modifier_nom(self,nom):
        self._nom = nom
    
    def modifier_prenom(self,prenom):
        self._prenom = prenom

    def modifier_civilite(self,civilite):
        self._civilite = civilite
    
    def modifier_date_de_naissance(self,date):
        self._date_de_naissance = date
    
    def modifier_email(self,mail):
        self.email = mail
    
    def default(self):
        print("Erreur : Aucun changement effectué")
    
    def modifier_profil(self):
        choix  = 0 
        while choix > 6 or choix < 1 :
            choix = int(input(' 1. Modifier le mot de passe \n'
            '2. Modifier le nom \n'
            '3. Modifier le prenom \n'
            '4. Modifier la civilité \n'
            '5. Modifier la date de naissance \n'
            '6. Modifier l\'adresse mail \n'
            'Taper le numéro correspondant :'))
            actions = {1: self.modifier_mdp,2:self.modifier_nom,3:self.modifier_prenom,4:self.modifier_civilite,
            5:self.modifier_date_de_naissance,6:self.modifier_email}
            action = actions.get(choix, self.default)
            action(input("entrer la nouvelle valeur :"))
        

    def type_abonnement(self):
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
        return 'Profil de {}. {} {} :\n Email: {} \n Date de naissance : {} '.format(self._civilite,self._nom, self._prenom,self.email,self._date_de_naissance)  


