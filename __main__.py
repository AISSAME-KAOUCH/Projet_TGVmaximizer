from DAO.db_connection import DBConnection
from business_object.profil import Profil
import requests
import utils
from DAO.profilDAO import ProfilDAO





profil = Profil('ilyass', 'el fikri', '13/12/2001','mr', 'mail', 'pass')
profildao = ProfilDAO()
profildao.create_profil(profil)