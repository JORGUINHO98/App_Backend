from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cineapp import views
from cineapp.views_auth import RegisterView, ProfileView, EmailTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView 

router = routers.DefaultRouter()
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"roles", views.RolViewSet)
router.register(r"permisos", views.PermisoViewSet)
router.register(r"favoritos", views.FavoritoViewSet)
router.register(r"vistos", views.VistoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    # Auth
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/profile/", ProfileView.as_view(), name="profile"),
    path("api/token/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
