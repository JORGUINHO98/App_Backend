from rest_framework import serializers
from .models import Usuario, Rol, Permiso, Favorito, Visto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "email", "nombre", "is_active", "is_staff"]

# Registro de usuario (maneja password)
class UsuarioRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ["id", "email", "nombre", "password"]

    def create(self, validated_data):
        user = Usuario(
            email=validated_data["email"],
            nombre=validated_data.get("nombre", "")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = "__all__"


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = "__all__"


class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = "__all__"


class VistoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visto
        fields = "__all__"
