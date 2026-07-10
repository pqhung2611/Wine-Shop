"""
Django REST Framework configuration.
"""

REST_FRAMEWORK = {
    # Authentication
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],

    # Permission
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],

    # Pagination
    "DEFAULT_PAGINATION_CLASS": "shared.pagination.pagination.StandardPagination",
    "PAGE_SIZE": 20,

    # Exception Handler
    "EXCEPTION_HANDLER": "shared.exceptions.handlers.custom_exception_handler",

    # Schema
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}