from rest_framework.exceptions import APIException
from rest_framework import status


class BusinessException(APIException):
    """
    Base business exception for the application.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Business validation failed."
    default_code = "business_error"