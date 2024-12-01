from typing import Type
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Model
from .filter.extremeFilter import ExtremeFilter
from .BaseSerializer import BaseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class BaseAPI(APIView):
    model: Type[Model] = None
    fields: list[str] = ["__all__"]
    extreme_filter: bool = False
    login_user: str = None
    permission_classes = [AllowAny]
    
    
    
    def get(self, request, *args, **kwargs):
        objects = self.model.objects.all()
        if self.login_user and request.user.is_authenticated:
            objects = objects.filter(**{self.login_user: request.user})
        elif self.login_user and not request.user.is_authenticated:
            return Response({'message': 'If you want to use this feature, please login or remove login_user parameter'},status=401)
        if request.GET.get('id'):
            try:
                object = objects.get(id=request.GET.get('id'))
            except self.model.DoesNotExist:
                return Response(status=404)
            serializer = BaseSerializer(object, model=self.model, fields=self.fields)
            return Response(serializer.data)
        objects = ExtremeFilter(self.model).filter(request) if self.extreme_filter else objects
        serializer = BaseSerializer(objects, many=True, model=self.model, fields=self.fields)
        return Response(serializer.data)