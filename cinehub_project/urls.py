from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from cineapp import views
from cineapp import views_auth
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# 👇 Página de bienvenida en HTML
def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CineHub API</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0;
                   margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .card { background: #1e293b; padding: 50px; border-radius: 16px;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.5); text-align: center; max-width: 600px; width: 90%;
                    animation: fadeIn 1s ease-in-out; }
            h1 { font-size: 2.8rem; margin-bottom: 15px; color: #facc15; }
            p { font-size: 1.1rem; margin-bottom: 30px; color: #94a3b8; }
            .btn { display: inline-block; margin: 8px; padding: 12px 24px; font-size: 1rem;
                   font-weight: bold; background: #facc15; color: #000; text-decoration: none;
                   border-radius: 10px; transition: all 0.3s ease; }
            .btn:hover { background: #eab308; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
            footer { margin-top: 20px; font-size: 0.9rem; color: #64748b; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); }
                                to { opacity: 1; transform: translateY(0); } }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎬 CineHub API</h1>
            <p>Bienvenido al backend de CineHub. Usa los siguientes enlaces para explorar los endpoints:</p>
            <div>
                <a class="btn" href="/api/">📌 API Root</a>
                <a class="btn" href="/admin/">⚙️ Admin</a>
                <a class="btn" href="/api/register/">📝 Registro</a>
                <a class="btn" href="/api/token/">🔑 Token</a>
                <a class="btn" href="/api/profile/">👤 Perfil</a>
            </div>
            <footer>© 2025 CineHub - Backend API</footer>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


# Routers para tus modelos
router = routers.DefaultRouter()
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"roles", views.RolViewSet)
router.register(r"permisos", views.PermisoViewSet)
router.register(r"favoritos", views.FavoritoViewSet)
router.register(r"vistos", views.VistoViewSet)

urlpatterns = [
    path("", home),  
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    # 🔑 Autenticación con JWT
    path("api/register/", views_auth.RegisterView.as_view(), name="register"),
    path("api/profile/", views_auth.ProfileView.as_view(), name="profile"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
