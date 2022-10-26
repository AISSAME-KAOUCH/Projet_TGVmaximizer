import datetime as dt
class Information:
    def __init__(self,date,heure,ville) -> None:
        self.date=date
        self.heure=heure
        self.ville=ville
    
    def __str__(self): 
        self.date = dt.datetime.strptime(self.date,'%d-%m-%Y').strftime('%d-%m-%Y')
        self.heure = dt.datetime.strptime(self.heure , '%H:%M:%S').time()
        return 'Gare : {}, le {}, à {}'.format(self.ville, self.date,self.heure)


if __name__=='__main__':
    info = Information('19-07-2022','13:23:00','Rennes')
    print(info)
