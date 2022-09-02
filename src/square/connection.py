from enum import Enum
from square.client import Client, CatalogApi

class ConnectionEnvironment(Enum):
    SANDBOX = 'sandbox'
    PRODUCTION = 'production'


class CatalogObjectType(Enum):
    

class SquareConnection:
    def __init__(self, access_token: str, environment: ConnectionEnvironment):
        self.__client = Client(access_token=access_token, environment=environment)
        self.__catalog: CatalogApi = self.__client.catalog

    def get_square_client(self):
        return self.__client

    def pull_catalog(self):
        self.__catalog.list_catalog()

    def push_catalog(self, catalog):
        pass



x = SquareConnection()

    


