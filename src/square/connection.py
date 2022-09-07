from enum import Enum, Flag
from typing import Any, Callable
from square.client import Client, CatalogApi
from square.http.api_response import ApiResponse

class ConnectionEnvironment(Enum):
    SANDBOX = 'sandbox'
    PRODUCTION = 'production'


class CatalogObjectType(Flag):
    NOTHING = 0
    ITEM = 1 << 0
    ITEM_VARIATION = 1 << 1
    MODIFIER = 1 << 2
    MODIFIER_LIST = 1 << 3
    CATEGORY = 1 << 4
    DISCOUNT = 1 << 5
    TAX = 1 << 6
    IMAGE = 1 << 7
    ALL = (1 << 8) - 1

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

    def stringify_set(self) -> str:
        actives = []
        for i, v in enumerate(CatalogObjectType.__object_type_strings):
            if bool(self & (1 << i)):
                actives.append(v)
        return ", ".join(actives)

    def stringify_one(self) -> str:
        for i, v in enumerate(CatalogObjectType.__object_type_strings):
            if self == (1 << i):
                return v
        raise ValueError("Expected exactly one object type.")
    
    def parse_set(s: str):
        actives = s.split(",")
        tot = CatalogObjectType.NOTHING
        for sub in actives:
            sub = sub.trim()
            tot: CatalogObjectType = tot | CatalogObjectType.parse_one(sub)
        return tot

    def parse_one(s: str):
        try:
            v: CatalogObjectType = CatalogObjectType.__string_object_types[s]
        except:
            raise ValueError("Unrecognized catalog object type name.")
        return v


class ResponsePages:
    def __init__(self, next_fn: Callable[[Any | None], ApiResponse]):
        self.__cursor = None
        self.__next = next_fn

    def advance(self):
        response = self.__next(self.__cursor)
        if response.is_error():
            response.errors
            raise RuntimeError("Square API failed with errors")
            
        
        

class SquareConnection:
    def __init__(self, access_token: str, environment: ConnectionEnvironment):
        self.__client = Client(access_token=access_token, environment=environment)
        self.__catalog: CatalogApi = self.__client.catalog

    def get_square_client(self):
        return self.__client

    def list_catalog(self, object_types: CatalogObjectType):
        def get_next_page(cursor): 
            return self.__catalog.list_catalog(cursor=cursor, types=object_types)
            
        return ResponsePages(get_next_page)

    def push_catalog(self):
        pass



if __name__ == "__main__":
    sq = SquareConnection("EAAAEPSHUwqyX4cuP-gETGVsfrbblpfaVnUc_VFfsZbe7ZHBnOhzXBcfKZqq_yx8", ConnectionEnvironment.SANDBOX)
    sq.get_square_client()
    


