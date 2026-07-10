from django.contrib import admin
from django.utils import timezone


class BaseAdmin(admin.ModelAdmin):
    """
    Base ModelAdmin shared by all models.

    This class only contains common configurations that are applicable
    to every model inheriting from TimeStampedModel/AuditModel.
    """

    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )

    ordering = ("-created_at",)

    list_per_page = 50

    def save_model(self, request, obj, form, change):
        """
        Automatically populate audit fields.
        """

        if not change and getattr(obj, "created_by", None) is None:
            obj.created_by = request.user

        if hasattr(obj, "updated_by"):
            obj.updated_by = request.user

        super().save_model(request, obj, form, change)


class SoftDeleteAdmin(BaseAdmin):
    """
    Base admin for models supporting soft delete.
    """

    readonly_fields = BaseAdmin.readonly_fields + (
        "deleted_at",
        "deleted_by",
    )

    list_filter = (
        "is_active",
        "is_deleted",
        "created_at",
    )

    actions = (
        "soft_delete_selected",
        "restore_selected",
    )

    @admin.action(description="Soft delete selected records")
    def soft_delete_selected(self, request, queryset):
        queryset.update(
            is_deleted=True,
            deleted_at=timezone.now(),
            deleted_by=request.user,
        )

    @admin.action(description="Restore selected records")
    def restore_selected(self, request, queryset):
        queryset.update(
            is_deleted=False,
            deleted_at=None,
            deleted_by=None,
        )