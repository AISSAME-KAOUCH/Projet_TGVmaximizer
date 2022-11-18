import datetime as dt

def type_abonnement_general(date):
    date = dt.datetime.strptime(date,'%d-%m-%Y').date()
    age = (dt.date.today() - date).days
    if age > 5840 and age < 9855 : # = ou >= ?
        res = True
    elif age > 21900 :
        res = True
    else : 
        res = False
    return res 