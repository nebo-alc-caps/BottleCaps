from enum import Flag
from socket import CAN_RAW


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



class CatalogObject:
    def __init__(self, obj_type: CatalogObjectType, id: str, version: int):
        self.type = obj_type.stringify_one()
        self.id = obj_type
        self.version = version


class CatalogObjectItem(CatalogObject):
    def __init__(self, id: str, version: int):
        super().__init__(CatalogObjectType.ITEM, id, version)
        self.item_data = {
            
        }

    def get_id(self):
        return self.id