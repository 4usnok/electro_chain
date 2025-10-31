from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from network.models import Network


class NetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Network"""
    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ('debt_fact',)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token