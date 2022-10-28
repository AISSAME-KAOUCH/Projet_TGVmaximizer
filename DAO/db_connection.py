import os
import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from utils.singleton import Singleton

class DBConnection(metaclass=Singleton):
    """
    Classe technique qui permet de générer une connection à la DB.
    """

    def __init__(self):

        """ Constructeur qui permet la création d'une connection.

        Parameters
        ----------

        Returns 
        -------

        """
    
        dotenv.load_dotenv(override=True) 
        self.__connection =psycopg2.connect(
            host=os.environ["HOST"],
            port=os.environ["PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)

    @property
    def connection(self):
        """
        Parameters
        ----------

        Returns 
        -------
        The opened connection 
        """

        return self.__connection