from django.db import models
from django.utils import timezone


class BaseQuerySet(models.QuerySet):
    """
    Base QuerySet providing common filtering
    and soft delete operations.
    """

    def active(self):
        return self.filter(
            is_active=True,
            is_deleted=False,
        )

    def inactive(self):
        return self.filter(
            is_active=False,
            is_deleted=False,
        )

    def alive(self):
        return self.filter(
            is_deleted=False,
        )

    def deleted(self):
        return self.filter(
            is_deleted=True,
        )

    def created_today(self):
        today = timezone.localdate()
        return self.filter(created_at__date=today)

    def created_this_month(self):
        today = timezone.localdate()
        return self.filter(
            created_at__year=today.year,
            created_at__month=today.month,
        )

    # Xóa mềm (.soft_delete()), Xóa thật (.delete())  
    def soft_delete(self):
        return self.update(
            is_deleted=True,
            deleted_at=timezone.now(),
        )

    def restore(self):
        return self.update(
            is_deleted=False,
            deleted_at=None,
            deleted_by=None,
        )