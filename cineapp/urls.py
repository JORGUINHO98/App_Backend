from django.urls import path
from . import views

urlpatterns = [
    # Rutas Películas
    path('peliculas/', views.peliculas, name='peliculas'),
    path('peliculas/<int:pk>/', views.pelicula_detalle, name='pelicula_detalle'),

    # Rutas Usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/<int:pk>/', views.usuario_detalle, name='usuario_detalle'),

    # Usuarios por Rol
    path('usuarios/por-rol/', views.show_by_rol, name='usuarios_por_rol'),

    # 🚀 Rutas TMDb
    path('tmdb/populares/', views.tmdb_populares, name='tmdb_populares'),
    path('tmdb/buscar/', views.tmdb_buscar, name='tmdb_buscar'),
    path('tmdb/guardar/', views.tmdb_guardar, name='tmdb_guardar'),
        # 🚀 Rutas TMDb - Favoritos
    path('tmdb/favorito/<int:usuario_id>/', views.tmdb_guardar_favorito, name='tmdb_guardar_favorito'),
    path('tmdb/favorito/<int:usuario_id>/<int:pelicula_id>/', views.tmdb_quitar_favorito, name='tmdb_quitar_favorito'),

]
