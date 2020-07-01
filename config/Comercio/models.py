from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=243)
    def __str__(self):
        return str(self.nombre)

class Ciudad(models.Model):
    nombre = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.nombre)

class Comuna(models.Model):
    nombre = models.CharField(max_length = 20)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.nombre)

class Direccion(models.Model):
    numero = models.CharField(max_length = 5)
    calle = models.CharField(max_length = 20)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str("{}, {}".format(self.calle,self.numero))

class Cliente(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.nombre)

class Venta(models.Model, Producto, Detalle):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descuento = models.IntegerField()
    monto_final = models.FloatField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, null=False)

    def MontoFinal(self, Detalle.cantidad, Producto.precio):
        cantidad = Detalle.cantidad
        precio = Producto.precio
        monto_final = cantidad * precio

    def __str__(self):
        return str("{}: {} (${})".format(self.fecha, self.cliente.nombre,self.montoFinal))

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    web = models.CharField(max_length=150)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=False)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str("{} (${})".format(self.nombre,self.precio))

class Detalle(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=False)
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str("({}) {} a {}".format(self.cantidad,self.producto.nombre,self.venta.cliente.nombre))
