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
    
    def modifier_profil(self):
        info = ["civilite", "nom", "prenom", "date_de_naissance"]
        attribut = []
        for i in range(0,4) : 
            res = input('Voulez-vous modifier votre {} ? (Oui/Non)'.format(info[i]))
            if res == 'Oui' : 
                if i ==3 : 
                    attribut.append(input("Quelle est votre modification (JJ-MM-YYYY) ?"))
                else :
                    attribut.append(input("Quelle est votre modification ?"))
            else : 
                attribut.append(None)
        if attribut[0] is not None : 
            self._civilite = attribut[0] 
        if attribut[1] is not None : 
            self._nom = attribut[1] 
        if attribut[2] is not None : 
            self._prenom = attribut[2] 
        if attribut[3] is not None : 
            self._date_de_naissance = attribut[3] 


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


