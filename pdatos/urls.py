from django.urls import path
from .views import DatosListView
from . import views

urlpatterns = [
    path('index_datos/', views.index_datos, name='index_datos'),
    path('insert/', views.insertData, name='insert'),
    path('update/<int:id>/', views.updateData, name='updateData'),
    path('delete/<int:id>/', views.deleteData, name='deleteData'),
    path('buscar/', views.buscar, name='buscar'),
    path('datos_list', DatosListView.as_view(), name='datos_list'),

]

