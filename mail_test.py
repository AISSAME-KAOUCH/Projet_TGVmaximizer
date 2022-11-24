from mail import creer_alerte
from business_object.recherches.recherche_aller import Recherche_aller
from business_object.profil import Profil
from business_object.trajet import Trajet

profil = Profil("M", "Emma", "Heard", "14-02-2001", "jules.lejas@gmail.com", "mot_de_passe")
trajet = Trajet("4", "Paris", "02-12-2022", "14:00", "Bordeaux", "17:00", "4333")
trajet2 = Trajet("4", "Paris", "02-12-2022", "14:00", "Bordeaux", "17:00", "4333")

recherche = Recherche_aller(profil, trajet)

creer_alerte(recherche, trajet2)