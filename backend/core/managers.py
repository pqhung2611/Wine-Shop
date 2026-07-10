from django.db import models

from core.querysets import BaseQuerySet


class BaseManager(models.Manager.from_queryset(BaseQuerySet)):
    """
    Base manager that exposes all custom QuerySet methods.

    Every model using BaseManager automatically supports:
    - active()
    - inactive()
    - alive()
    - deleted()
    - created_today()
    - created_this_month()
    - soft_delete()
    - restore()
    """

    pass