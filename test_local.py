
from business_object.trajet import Trajet
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.profil import Profil

profil = Profil("Dupont", "Jean", "02-03-1980", "M", "jean.dupont@gmail.com", "first_mdp")

trajet = Trajet('0','Paris', '10-01-2022', '07:00', 'Rennes', '', '0', 'oui')
rech = Recherche_aller(profil, trajet)
rech.recherche(trajet)
    