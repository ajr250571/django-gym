from django.db import models
from django.utils import timezone


class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_alta = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'socios'
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Plan(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'planes'
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.nombre


class Membresia(models.Model):
    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('VENCIDA', 'Vencida'),
        ('CANCELADA', 'Cancelada'),
    ]

    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE, related_name='membresias')
    plan = models.ForeignKey(
        Plan, on_delete=models.PROTECT, related_name='membresias')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVA')

    def __str__(self):
        return f"{self.socio} - {self.plan}"

    class Meta:
        db_table = 'membresias'
        verbose_name = 'Membresia'
        verbose_name_plural = 'Membresias'


class Pago(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('VENCIDO', 'Vencido'),
    ]

    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateTimeField()
    estado = models.CharField(
        max_length=10, choices=ESTADOS, default='PENDIENTE')
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)
    comprobante_nro = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.socio} - {self.monto}"

    class Meta:
        db_table = 'pagos'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'


class Asistencia(models.Model):
    socio = models.ForeignKey(
        Socio, on_delete=models.CASCADE, related_name='asistencias')
    fecha_hora = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'asistencias'
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
