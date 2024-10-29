from functools import wraps
from rest_framework import status
from .response_utils import error_response
from .exceptions import BaseAPIException

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseAPIException as e:
            return error_response(str(e), e.status_code)
        except Exception as e:
            return error_response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper