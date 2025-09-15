from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  
    def __str__(self):
        return self.email
class Permiso(models.Model):
    descripcion = models.TextField(blank=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=150)
    permisos = models.ManyToManyField(Permiso, related_name="roles", blank=True)

    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="favoritos", 
        on_delete=models.CASCADE
    )
    id_pelicula = models.IntegerField()
    lista_de_pelicula = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Favorito {self.id_pelicula} de {self.usuario}"

class Visto(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="vistos", 
        on_delete=models.CASCADE
    )
    calificacion = models.IntegerField(null=True, blank=True)
    fecha_visto = models.DateTimeField(null=True, blank=True)
    nota_personal = models.TextField(blank=True)
    porcentaje_visto = models.IntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.titulo} visto por {self.usuario}"
