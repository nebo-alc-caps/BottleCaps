from enum import Enum
from square.client import Client

class ConnectionEnvironment(Enum):
    SANDBOX = 'sandbox'
    PRODUCTION = 'production'

class SquareConnection:
    def __init__(self, access_token: str, environment: ConnectionEnvironment):
        self.__client = Client(access_token=access_token, environment=environment)

    def get_square_client(self):
        return self.__client

class Catalog
    

    


