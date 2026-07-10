from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract model that provides created/updated timestamps.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text="Date and time when the record was created."
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the record was last updated."
    )

    class Meta:
        abstract = True


class AuditModel(TimeStampedModel):
    """
    Abstract model that tracks who created and updated the record.
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created",
        help_text="User who created this record."
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        help_text="User who last updated this record."
    )

    class Meta:
        abstract = True


class SoftDeleteModel(AuditModel):
    """
    Abstract model supporting soft delete.
    """

    is_active = models.BooleanField(
        default=True,
        db_index=True,
        help_text="Whether the record is active."
    )

    is_deleted = models.BooleanField(
        default=False,
        db_index=True,
        help_text="Whether the record has been soft deleted."
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Date and time when the record was deleted."
    )

    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_deleted",
        help_text="User who deleted this record."
    )

    class Meta:
        abstract = True