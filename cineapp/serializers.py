from rest_framework import serializers
from .models import Usuario, Rol, Permiso, Favorito, Visto

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class VistoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visto
        fields = '__all__'
