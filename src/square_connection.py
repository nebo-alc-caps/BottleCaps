from enum import Enum, Flag
from typing import Any, Callable
from urllib import request
import uuid
from square.client import Client, CatalogApi
from square.http.api_response import ApiResponse


def check_response(response: ApiResponse):
    if not response.is_success():
        raise RuntimeError(response)


class ConnectionEnvironment(Enum):
    SANDBOX = 'sandbox'
    PRODUCTION = 'production'

"""class ResponsePages:
    def __init__(self, next_fn: Callable[[Any | None], ApiResponse]):
        self.__cursor = None
        self.__next = next_fn

    def advance(self):
        response = self.__next(self.__cursor)
        if response.is_error():
            response.errors
            raise RuntimeError("Square API failed with errors")"""
            
        
class SquareRequest:
    def __init__(self):
        self.idempotency_key = str(uuid.uuid4())


DEFAULT_SANDBOX_KEY = "EAAAEPSHUwqyX4cuP-gETGVsfrbblpfaVnUc_VFfsZbe7ZHBnOhzXBcfKZqq_yx8"

class SquareConnection:
    def __init__(self, access_token: str, environment: ConnectionEnvironment):
        self.__client = Client(access_token=access_token, environment=environment)

    def get_square_client(self):
        return self.__client

    def get_default_sandbox():
        return SquareConnection(DEFAULT_SANDBOX_KEY, ConnectionEnvironment.SANDBOX.value)
    


