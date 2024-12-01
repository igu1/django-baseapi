from typing import Type
from django.db.models import Model
from .BaseAPI import BaseAPI


class CallableBaseAPI:
    def __init__(
        self,
        model: Type[Model],
        fields: list[str] | None = None,
        Xfilter: bool = False,
        permission_classes=[],
        depth=0,
        **kwargs
    ):
        self.model = model
        self.fields = fields
        self.Xfilter = Xfilter
        self.permission_classes = permission_classes
        self.depth = depth
        self.kwargs = kwargs

    def __call__(self, request, *args, **kwargs):
        view = BaseAPI.as_view(
            model=self.model,
            fields=self.fields,
            extreme_filter=self.Xfilter,
            permission_classes=self.permission_classes,
            depth=self.depth,
            **self.kwargs
        )
        return view(request, *args, **kwargs)
