from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cineapp.urls')),  # Rutas de la app cineapp
    path('profile/update/', views.update_profile, name='update_profile'),

]
