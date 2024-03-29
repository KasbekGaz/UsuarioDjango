from rest_framework import serializers
from .models import CustomUser, Obra, Gasto


class CustomUserSerializer(serializers.ModelSerializer):
    rol = serializers.ChoiceField(choices=CustomUser.ROL_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'telefono', 'password', 'rol')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            telefono=validated_data.get('telefono'),
            rol=validated_data['rol']
        )
        return user


class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'


class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'
