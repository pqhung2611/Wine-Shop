from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


class GetMixin:
    @classmethod
    def get(cls, **filters):
        try:
            return cls.get_queryset().get(**filters)
        except ObjectDoesNotExist:
            raise cls.model.DoesNotExist(
                f"{cls.model.__name__} does not exist."
            )


class CreateMixin:
    @classmethod
    @transaction.atomic
    def create(cls, **data):
        return cls.get_queryset().create(**data)


class UpdateMixin:
    @classmethod
    @transaction.atomic
    def update(cls, instance, **data):
        for field, value in data.items():
            setattr(instance, field, value)

        instance.save()

        return instance


class SoftDeleteMixin:
    @classmethod
    @transaction.atomic
    def soft_delete(cls, instance):
        instance.is_deleted = True
        instance.save(update_fields=["is_deleted"])

        return instance


class RestoreMixin:
    @classmethod
    @transaction.atomic
    def restore(cls, instance):
        instance.is_deleted = False
        instance.save(update_fields=["is_deleted"])

        return instance