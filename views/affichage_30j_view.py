from PyInquirer import  prompt
from views.abstract_view import AbstractView
from views.session import Session
from business_object.trajet import Trajet
from business_object.profil import Profil

class Recherche30jView(AbstractView):
    def __init__(self) -> None: 
        
