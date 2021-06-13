from rest_framework.serializers import ModelSerializer

from .models import UserRequest, Client


class UserRequestSerializer(ModelSerializer):

    class Meta:
        model = UserRequest
        fields = '__all__'


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
