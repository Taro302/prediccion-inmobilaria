from django.views.generic import ListView
from .models import bdatos
from django.shortcuts import render, redirect
from django.contrib import messages

class BdatosManager:
    def get_all_data(self):
        return bdatos.objects.all()


def index_datos(request):
    manager = BdatosManager()
    data = manager.get_all_data()
    print(data)
    context={"data":data}
    return render(request, "index_datos.html", context)

# PARA INSERTAR DATOS ESTA BIEN
def insertData(request):
    if request.method == "POST":
        # Obtener los datos del formulario POST y guardarlos en la base de datos
        tamanio = request.POST.get('tamanio')
        habitaciones = request.POST.get('habitaciones')
        banos = request.POST.get('banos')
        estacionamiento = request.POST.get('estacionamiento')
        piscina = request.POST.get('piscina')
        distrito = request.POST.get('distrito')
        precio = request.POST.get('precio')

        query = bdatos(
            tamanio=tamanio,
            habitaciones=habitaciones,
            banos=banos,
            estacionamiento=estacionamiento,
            piscina=piscina,
            distrito=distrito,
            precio=precio
        )
        query.save()

        # Redirigir a la misma página para actualizar la tabla
        return redirect('insert')  # Reemplaza 'index_datos' con el nombre de tu URL correspondiente

    elif request.method == "GET":
        # Obtener todos los datos de la base de datos
        datos = bdatos.objects.all()

        # Renderizar la página con los datos actualizados
        context = {
            'data': datos,
        }
        return render(request, 'index_datos.html', context)




def buscar(request):
    tamanio = request.GET.get('buscar_tamanio')
    distrito = request.GET.get('buscar_distrito')
    habitaciones = request.GET.get('buscar_habitaciones')
    banos = request.GET.get('buscar_banos')
    piscina = request.GET.get('buscar_piscina')
    precio = request.GET.get('buscar_precio')

    manager = BdatosManager()
    datos = manager.get_all_data()

    if tamanio:
        datos = datos.filter(tamanio=tamanio)

    if distrito:
        datos = datos.filter(distrito=distrito)

    if habitaciones:
        datos = datos.filter(habitaciones=habitaciones)

    if banos:
        datos = datos.filter(banos=banos)

    if piscina:
        datos = datos.filter(piscina=piscina)

    if precio:
        datos = datos.filter(precio=precio)

    context = {
        'data': datos,
        'buscar_tamanio': tamanio,
        'buscar_distrito': distrito,
        'buscar_habitaciones': habitaciones,
        'buscar_banos': banos,
        'buscar_piscina': piscina,
        'buscar_precio': precio
    }
    return render(request, 'index_datos.html', context)


# PARA ACTUALIZAR DATOS 
from django.shortcuts import get_object_or_404

def updateData(request, id):
    dato = get_object_or_404(bdatos, id=id)

    if request.method == "POST":
        # Obtener los datos del formulario POST y guardar los cambios en la base de datos
        tamanio = request.POST.get('tamanio')
        habitaciones = request.POST.get('habitaciones')
        banos = request.POST.get('banos')
        estacionamiento = request.POST.get('estacionamiento')
        piscina = request.POST.get('piscina')
        distrito = request.POST.get('distrito')
        precio = request.POST.get('precio')

        dato.tamanio = tamanio
        dato.habitaciones = habitaciones
        dato.banos = banos
        dato.estacionamiento = estacionamiento
        dato.piscina = piscina
        dato.distrito = distrito
        dato.precio = precio
        dato.save()

        return redirect('index_datos')  # Redirigir a la página de índice de datos (o a la URL que desees)

    elif request.method == "GET":
        context = {
            'd': dato,
        }
        return render(request, 'edit.html', context)




# PARA ELIMINAR CAMPP


def deleteData(request, id):
    dato = get_object_or_404(bdatos, id=id)

    if request.method == "POST":
        dato.delete()
        messages.warning(request, "Datos eliminados exitosamente")
        return redirect('index_datos')

    # Redireccionar al index_datos si no es una solicitud POST
    return redirect('index_datos')



class DatosListView(ListView):
    model = bdatos
    template_name = 'datos_list.html'
    context_object_name = 'datos'

