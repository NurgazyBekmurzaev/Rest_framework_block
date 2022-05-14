from . import serializers
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .models import MyUser

class UserViewSet(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = serializers.UserSerializer