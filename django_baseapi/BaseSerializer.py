from typing import Type
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.db.models import Model, ForeignKey
from .filter.extremeFilter import ExtremeFilter


class BaseSerializer(serializers.ModelSerializer):

    def __init__(
        self,
        *args,
        model: Type[Model] = None,
        fields: list[str] | None = None,
        depth: int = 0,
        **kwargs
    ):
        assert model is not None, "You must provide a model class."
        self.Meta.model = model

        if fields:
            fields = self._process_fields(fields, model)
            self.Meta.fields = fields
        else:
            self.Meta.fields = "__all__"

        if self._get_foreign_keys(model) and depth != 0:
            setattr(self.Meta, "depth", self._auto_set_depth(model))

        super().__init__(*args, **kwargs)

    def _process_fields(self, fields: list[str], model: Type[Model]) -> list[str]:
        return [field for field in fields if not field.startswith("!")]

    def _get_foreign_keys(self, model: Type[Model]) -> list[str]:
        return [
            field.name
            for field in model._meta.get_fields()
            if isinstance(field, ForeignKey)
        ]

    def _auto_set_depth(self, model: Type[Model]) -> int:
        return self._calculate_depth(model)

    def _calculate_depth(self, model: Type[Model], visited: set = None) -> int:
        if visited is None:
            visited = set()
        if model in visited:
            return 0
        visited.add(model)
        max_depth = 0
        for field in model._meta.get_fields():
            if isinstance(field, ForeignKey):
                related_model = field.related_model
                max_depth = max(
                    max_depth, self._calculate_depth(related_model, visited)
                )
        return max_depth + 1

    class Meta:
        model = None
        fields = "__all__"
        depth = 0
