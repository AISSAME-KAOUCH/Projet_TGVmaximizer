import datetime as dt

class Information :
    def __init__(self, date, heure, ville):
        self.date = date
        self.heure = heure
        self.ville = ville
    
    def __str__(self): 
        self.date = dt.datetime.strptime(self.date,'%d-%m-%Y').strftime('%d-%m-%Y')
        self.heure = dt.datetime.strptime(self.heure,'%H:%M:%S').time()
        return 'Ville : {}, le {}, à {}'.format(self.ville, self.date, self.heure)






