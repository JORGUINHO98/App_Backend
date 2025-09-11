from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cineapp import views

router = routers.DefaultRouter()
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"roles", views.RolViewSet)
router.register(r"permisos", views.PermisoViewSet)
router.register(r"favoritos", views.FavoritoViewSet)
router.register(r"vistos", views.VistoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
