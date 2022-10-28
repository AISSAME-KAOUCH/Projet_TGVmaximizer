from information import Information

class Trajet : 

    def __init__(self, id, ville_depart, date_depart, heure_depart,
                ville_arrivee = None, date_arrivee = None, heure_arrivee = None, numero_train = None):
        self.id = id
        self.ville_depart = ville_depart 
        self.date_depart = date_depart
        self.heure_depart = heure_depart
        self.ville_arrivee = ville_arrivee
        self.date_arrivee = date_arrivee
        self.heure_arrivee = heure_arrivee
        self.numero_train = numero_train

    
    def __str__(self):
        return 'Trajet au départ de {} le {} à {}, arrivée prévue à {} le {} à {}.'.format(self.ville_depart,self.date_depart,self.heure_depart,self.ville_arrivee,self.date_arrivee,self.heure_arrivee)


