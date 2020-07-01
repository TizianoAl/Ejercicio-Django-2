from django.contrib import admin
from .models import *


class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['rut', 'nombre', 'telefono',]
    list_display = ['rut', 'nombre', 'telefono',]
    list_display_links = ['rut', 'nombre',]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'proveedor',]
    fieldsets = (
        ("Descripcion", {
            'fields':('nombre', 'categoria', 'proveedor',)
        }),
        ('Variables', {
            'fields':('precio', 'stock',)
        }),
    )

class ProductoInLine(admin.TabularInline):
    model = Producto
    fields = ['nombre', 'categoria', 'precio', 'stock', 'proveedor',]

class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'rut']
    list_display = ['nombre', 'telefono', 'direccion']
    list_display_links = ['nombre', 'telefono', 'direccion']
    inlines = [ProductoInLine]

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente','isDescuento','fecha')
    list_display_links = ('cliente','fecha',)
    actions = ['hacer_Descuento', 'quitar_Descuento']
    def hacer_Descuento(self,request,queryset):
        return queryset.update(descuento = True)
    def quitar_Descuento(self,request,queryset):
        return queryset.update(descuento = False)
        

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Detalle)
