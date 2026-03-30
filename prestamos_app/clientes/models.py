from django.db import models
from decimal import Decimal

class Cliente(models.Model):
    INTERES_CHOICES = [
        (7, '7%'),
        (8, '8%'),
        (9, '9%'),
    ]

    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    capital = models.DecimalField(max_digits=10, decimal_places=2)
    interes = models.IntegerField(choices=INTERES_CHOICES)

    porcentaje_total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_trabajador = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_gastos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_reinversion = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    monto_trabajador = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_ganancia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_reinversion = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    ampliacion_prestamo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    abonos_capital = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

def calcular_porcentajes(self):
        interes = self.interes

        # Reset
        self.porcentaje_gastos = Decimal('0')

        if interes == 7:
            self.porcentaje_trabajador = Decimal('2')
            self.porcentaje_ganancia = Decimal('2')
            self.porcentaje_reinversion = Decimal('3')

        elif interes == 8:
            self.porcentaje_trabajador = Decimal('2')
            self.porcentaje_ganancia = Decimal('2')
            self.porcentaje_gastos = Decimal('1')
            self.porcentaje_reinversion = Decimal('3')

        elif interes == 9:
            self.porcentaje_trabajador = Decimal('2')
            self.porcentaje_ganancia = Decimal('2')
            self.porcentaje_gastos = Decimal('2')
            self.porcentaje_reinversion = Decimal('3')

        # Total
        self.porcentaje_total = (
            self.porcentaje_trabajador +
            self.porcentaje_ganancia +
            self.porcentaje_gastos +
            self.porcentaje_reinversion
        )

def calcular_montos(self):
        capital = self.capital

        self.monto_trabajador = (capital * self.porcentaje_trabajador) / 100
        self.monto_ganancia = (capital * self.porcentaje_ganancia) / 100
        self.monto_gastos = (capital * self.porcentaje_gastos) / 100
        self.monto_reinversion = (capital * self.porcentaje_reinversion) / 100

def save(self, *args, **kwargs):
        self.calcular_porcentajes()
        self.calcular_montos()
        super().save(*args, **kwargs)

def __str__(self):
        return self.nombre


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos')

    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    realizado = models.BooleanField(default=False)
    monto_pendiente = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    dias_atraso = models.IntegerField(default=0)

    def calcular_multa(self):
        return (self.cliente.capital / Decimal('1000')) * Decimal('15') * self.dias_atraso