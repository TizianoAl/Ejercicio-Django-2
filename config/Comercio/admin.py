from django.contrib import admin
from .models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['rut', 'nombre', 'telefono',]
    list_display = ['rut', 'nombre', 'telefono',]
    list_display_links = ['rut', 'nombre',]







admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Venta)
