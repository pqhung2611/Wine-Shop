import logging

from django.db import IntegrityError
from rest_framework import status
from rest_framework.views import exception_handler

from shared.responses.responses import ApiResponse

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Global DRF exception handler.
    """

    response = exception_handler(exc, context)

    # Handle DRF exceptions
    if response is not None:
        return ApiResponse.error(
            message=response.data.get("detail", "Request failed."),
            errors=response.data,
            status_code=response.status_code,
        )

    # Handle database integrity errors
    if isinstance(exc, IntegrityError):
        logger.exception(exc)

        return ApiResponse.error(
            message="Database integrity error.",
            errors=str(exc),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Handle unexpected exceptions
    logger.exception(exc)

    return ApiResponse.error(
        message="Internal server error.",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )