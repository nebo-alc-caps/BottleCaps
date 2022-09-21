from enum import Flag
from optparse import check_choice
from square_connection import *

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

    def get_id(self):
        return self.id


class CatalogObjectVariation(CatalogObject):
    def __init__(self, id: str, name: str, version: int = 0):
        super().__init__(CatalogObjectType.ITEM, id, version)
        self.item_data = {
            
        }

class CatalogObjectItem(CatalogObject):
    def __init__(self, id: str, name: str, variations: list[CatalogObjectVariation], version: int = 0):
        super().__init__(CatalogObjectType.ITEM, id, version)
        self.item_data = {
            variations
        }

MAX_BATCH_SIZE = 1000

class CatalogObjectBatch:
    def __init__(self, objects: list[CatalogObject]):
        if len(objects) > MAX_BATCH_SIZE:
            raise ValueError("Batch size exceeded the maximum batch size")
        self.objects = objects


class CatalogBatchUpsertRequest(SquareRequest):
    def __init__(self, batches: list[CatalogObjectBatch]):
        super().__init__()
        self.batches = batches

class SquareCatalog:
    def __init__(self, s: SquareConnection):
        self.__catalog: CatalogApi = s.get_square_client().catalog
        self.new_objects: dict[str, CatalogObject]

    def register_new(self, obj: CatalogObject):
        if not obj.id in self.objects:
            self.objects[obj.id] = obj
        else:
            raise ValueError("Object id already present.")

    def batch_upsert(self, request: CatalogBatchUpsertRequest):
        response = self.__catalog.batch_upsert_catalog_objects(request)
        check_response(response)
        body = response.body
        id_map = body.id_mappings
        for el in id_map:
            our_id = el.client_object_id
            o = self.new_objects[our_id]
            o.id = el.object_id
            del self.new_objects[our_id]
