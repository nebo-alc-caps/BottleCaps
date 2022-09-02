from enum import Enum, Flag, auto
from square.client import Client, CatalogApi

class ConnectionEnvironment(Enum):
    SANDBOX = 'sandbox'
    PRODUCTION = 'production'


class CatalogObjectType(Flag):
    ITEM = 1 << 0
    ITEM_VARIATION = 1 << 1
    MODIFIER = 1 << 2
    MODIFIER_LIST = 1 << 3
    CATEGORY = 1 << 4
    DISCOUNT = 1 << 5
    TAX = 1 << 6
    IMAGE = 1 << 7


    __object_type_strings = [
        "ITEM", 
        "ITEM_VARIATION", 
        "MODIFIER", 
        "MODIFIER_LIST", 
        "CATEGORY",
        "DISCOUNT",
        "TAX",
        "IMAGE"
    ]

    __string_object_types = {
        v: (1 << k) for k, v in enumerate(__object_type_strings)
    }

    def stringify(self):
        actives = []
        for i, v in enumerate(CatalogObjectType.__object_type_strings):
            if self & (1 << i):
                actives.append(v)
        return ", ".join(actives)




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
    


