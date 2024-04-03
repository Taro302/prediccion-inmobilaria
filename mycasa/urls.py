from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cotizaciones', views.cotizaciones, name='cotizaciones'),
    path('predict/', views.predict_view, name='predict'),   
    path('propiedades', views.propiedades, name='propiedades'),
    path('contacto', views.contacto, name='contacto'),
    path('fots', views.fot, name='fots'),
  
]