from django.db import models

# Create your models here.

class Detalle(models.Model):
    cantidad = models.IntegerField()
    def __str__(self):
        return str(self.cantidad)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=243)
    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

class Venta(models.Model, Producto, Detalle):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descuento = models.FloatField()
    monto_final = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def MontoFinal(self, Detalle.cantidad, Producto.precio):
        cantidad = Detalle.cantidad
        precio = Producto.precio
        monto_final = cantidad * precio

    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    def __str__(self):
        return str(self.calle)

class Cliente(models.Model):
    RUT = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    #Falta Direccion
    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    RUT = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    WEB = models.CharField(max_length=150)
    #Falta Direccion
    def __str__(self):
        return str(self.nombre)
