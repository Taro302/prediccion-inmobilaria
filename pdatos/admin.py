
# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import bdatos, Sdatos

class BdatosAdmin(ImportExportModelAdmin):
    # Define los campos que deseas mostrar en la lista de registros en el admin
    list_display = ('tamanio', 'habitaciones', 'banos', 'estacionamiento', 'piscina', 'distrito', 'precio')
    search_fields=('tamanio', 'habitaciones', 'banos', 'estacionamiento', 'piscina', 'distrito', 'precio')
    list_filter =('tamanio', 'distrito')

# Registra el modelo y la clase de administración personalizada en el admin
admin.site.register(bdatos, BdatosAdmin)

admin.site.register(Sdatos)


