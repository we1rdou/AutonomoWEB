from django.db import models

class Mesa(models.Model):
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"Mesa {self.id} - {self.ubicacion} (Capacidad: {self.capacidad})"

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido {self.id} - Estado: {self.estado}"

class Plato(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()

    def __str__(self):
        return self.nombre
