from django.urls import path
from . import views
urlpatterns = [
    # Otras URLs de tu aplicación...
    path('', views.chatbots, name='chatbot'),

    path('getResponse',views.getResponse, name='getResponse'),
]
