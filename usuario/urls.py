from django.urls import path
from .views import HomeView, login_register_view
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', login_register_view, name='login_register'),  # Configura login_register_view como la página de inicio
    # Resto de las URL y vistas
    path('profile/', views.profile, name='profile'),

    path('home/', HomeView.as_view(), name='home'),

    path('logout/', views.LogoutPage, name='logout'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)