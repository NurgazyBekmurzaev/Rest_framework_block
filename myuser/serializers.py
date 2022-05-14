from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MyUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'username', 'posts', 'comments' ]