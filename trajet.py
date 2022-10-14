from information import Information

class Trajet : 

    def __init__(self, depart:Information, arrivee:Information):
        self.depart = depart 
        self.arrivee = arrivee
    
    def __str__(self):
        return 'Trajet au départ de {} le {} à {}, arrivée prévue à {} le {} à {}.'.format(self.depart.ville,self.depart.date,self.depart.heure,self.arrivee.ville,self.arrivee.date,self.arrivee.heure)


