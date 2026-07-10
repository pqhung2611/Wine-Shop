from core.services.mixins import (
    CreateMixin,
    GetMixin,
    RestoreMixin,
    SoftDeleteMixin,
    UpdateMixin,
)


class BaseService(
    GetMixin,
    CreateMixin,
    UpdateMixin,
    SoftDeleteMixin,
    RestoreMixin,
):
    """
    Base service inherited by every business service.
    """

    model = None

    @classmethod
    def get_queryset(cls):
        if cls.model is None:
            raise NotImplementedError(
                "Subclasses must define 'model'."
            )

        return cls.model.objects