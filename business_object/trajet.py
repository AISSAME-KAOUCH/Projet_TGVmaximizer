class Trajet : 

    "Trajet contenant les informations du voyage en train."

    def __init__(self, id, ville_depart, date_depart, heure_depart,
<<<<<<< HEAD
                ville_arrivee = None, date_arrivee = None, heure_arrivee = None, numero_train = None):
=======
                ville_arrivee, date_arrivee, heure_arrivee, numero_train):

        """ Constructeur permettant l'instanciation d'un objet Trajet.

        Parameters
        ----------
        id : str
            identifiant du trajet
        ville_depart : str
            ville de laquelle part le train correspondant au trajet
        date_depart : str
            date (JJ-MM-YYYY) à laquelle part le train correspondant au trajet
        heure_depart : str
            heure à laquelle part le train correspondant au trajet
        ville_arrivee : str
            ville dans laquelle arrive le train correspondant au trajet
        date_arrivee : str
            date à laquelle arrive le train correspondant au trajet
        heure_arrivee : str
            heure à laquelle arrive le train correspondant au trajet
        numero_train : str
            numero du train correspondant au trajet
        """

>>>>>>> 9de4cd91a1c81a7ed93c74e0bc6c7555fbb67d5c
        self.id = id
        self.ville_depart = ville_depart 
        self.date_depart = date_depart
        self.heure_depart = heure_depart
        self.ville_arrivee = ville_arrivee
        self.date_arrivee = date_arrivee
        self.heure_arrivee = heure_arrivee
        self.numero_train = numero_train

    
    def __str__(self):
        """ Fonction permettant d'afficher les information du trajet.

        Parameters
        ----------

        Returns
        -------
        str : les informations du trajet
        """
        return 'Trajet au départ de {} le {} à {}, arrivée prévue à {} le {} à {}.'.format(self.ville_depart,self.date_depart,self.heure_depart,self.ville_arrivee,self.date_arrivee,self.heure_arrivee)


