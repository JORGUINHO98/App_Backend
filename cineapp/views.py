from rest_framework import viewsets
from .models import Usuario, Rol, Permiso, Favorito, Visto
from .serializers import UsuarioSerializer, RolSerializer, PermisoSerializer, FavoritoSerializer, VistoSerializer
from rest_framework.generics import CreateAPIView
from .serializers import UsuarioRegisterSerializer

class RegisterView(CreateAPIView):
    serializer_class = UsuarioRegisterSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class VistoViewSet(viewsets.ModelViewSet):
    queryset = Visto.objects.all()
    serializer_class = VistoSerializer
