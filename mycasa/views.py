"""Module providingFunction printing python version."""
import pickle
import pandas as pd
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='login_register')



def home(request):
    return render(request, 'home.html')

def propiedades(request):
    return render(request, 'propiedades.html')

def contacto(request):
    return render(request, 'contacto.html')


def cotizaciones(request):
    return render(request, 'cotizaciones.html')


import locale

def predict_view(request):
    if request.method == 'POST':
        tamanio = int(request.POST.get('tamanio'))
        habitaciones = int(request.POST.get('habitaciones'))
        banos = int(request.POST.get('banos'))
        estacionamiento = int(request.POST.get('estacionamiento'))
        piscina = int(request.POST.get('piscina'))
        distrito = request.POST.get('distrito')

        # Cargar el modelo desde el archivo pkl
        with open('modeloCasas.pkl', 'rb') as archivo:
            modelo = pickle.load(archivo)

        # Crear un nuevo DataFrame con los datos ingresados por el usuario
        datos = {
            'TAMAÑO(M2)': [tamanio],
            'HABITACIONES': [habitaciones],
            'BAÑOS': [banos],
            'ESTACIONAMIENTO': [estacionamiento],
            'PISCINA': [piscina],
            'DISTRITO_Ate Vitarte': [int(distrito == 'Ate Vitarte')],
            'DISTRITO_La Molina': [int(distrito == 'La Molina')],
            'DISTRITO_Los Olivos': [int(distrito == 'Los Olivos')],
            'DISTRITO_San Isidro': [int(distrito == 'San Isidro')],
            'DISTRITO_San Miguel': [int(distrito == 'San Miguel')]
        }
        datos_df = pd.DataFrame(datos)
        # Establecer la configuración regional para el formato de números
        locale.setlocale(locale.LC_ALL, '')  # Utiliza la configuración regional predeterminada del sistema

        # Realizar la predicción
        prediccion = modelo.predict(datos_df)
        # Formatear la predicción como un número con comas
        prediccion_formateada = locale.format_string("%.2f", prediccion, grouping=True)

        return render(request, 'resultado.html', {'prediccion': prediccion_formateada})

    return render(request, 'cotizaciones.html')


def fot(request):
    return render(request, 'Perfil.html')
