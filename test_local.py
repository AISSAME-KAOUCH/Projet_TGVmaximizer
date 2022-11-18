from business_object.trajet import Trajet
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.profil import Profil
from client.trajet_client import Trajetclient
from DAO.trajetDAO import TrajetDAO

profil = Profil("Dupont", "Jean", "02-03-1980", "M", "jean.dupont@gmail.com", "first_mdp")
trajet = Trajet('0','RENNES', '08-12-2022', '09:35:00', 'LAVAL', '12:00:00', '22', 'oui')
rech = Recherche_aller(profil, trajet)
res = rech.recherche() 
for trj in res :
    print(trj.__str__())
