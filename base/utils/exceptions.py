from rest_framework.exceptions import APIException
from rest_framework import status

class BaseAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'An error occurred'
    default_code = 'error'

class InvalidCredentials(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Invalid credentials'
    default_code = 'invalid_credentials'

class ResourceNotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Resource not found'
    default_code = 'not_found'