from django.contrib import admin
from .models import Permiso, Rol, Usuario, Favorito, Visto

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre",)

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    filter_horizontal = ("permisos",)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "correo", "nombre")
    search_fields = ("username", "correo", "nombre")
    filter_horizontal = ("roles",)

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "id_pelicula", "lista_de_pelicula")
    search_fields = ("usuario__username", "id_pelicula")

@admin.register(Visto)
class VistoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "titulo", "calificacion", "fecha_visto", "porcentaje_visto")
    search_fields = ("usuario__username", "titulo")
    list_filter = ("fecha_visto", "calificacion")
