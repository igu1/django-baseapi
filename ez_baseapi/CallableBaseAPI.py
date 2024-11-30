from typing import Type
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.db.models import Model


class BaseSerializer(serializers.ModelSerializer):

    def __init__(self, *args, model: Type[Model] = None, **kwargs):
        if model:
            self.Meta.model = model
        super().__init__(*args, **kwargs)

    class Meta:
        model = None
        fields = "__all__"


class CallableBaseAPI:
    def __init__(self, model: Type[Model]):
        self.model = model

    def __call__(self, *args, **kwargs):
        view = BaseAPI.as_view(model=self.model)
        return view(*args, **kwargs)


class BaseAPI(APIView):
    model: Type[Model] = None

    def get(self, request, *args, **kwargs):
        query_params = {key: value for key, value in request.GET.items() if value}
        if query_params:
            objects = self.model.objects.filter(**query_params)
        else:
            objects = self.model.objects.all()
        serializer = BaseSerializer(objects, many=True, model=self.model)
        return Response(serializer.data)
