from django.db import models
from decimal import Decimal

class Cliente(models.Model):
    INTERES_CHOICES = [
        (7, '7%'),
        (8, '8%'),
        (9, '9%'),
    ]

    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100, default='General')
    capital = models.DecimalField(max_digits=10, decimal_places=2)
    interes = models.IntegerField(choices=INTERES_CHOICES)

    porcentaje_total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_trabajador = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_gastos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_reinversion = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        interes_decimal = Decimal(self.interes) / Decimal(100)

        self.porcentaje_total = self.capital * interes_decimal

        if self.interes == 7:
            self.porcentaje_trabajador = self.capital * Decimal('0.02')
            self.porcentaje_ganancia = self.capital * Decimal('0.02')
            self.porcentaje_gastos = Decimal('0.00')
            self.porcentaje_reinversion = self.capital * Decimal('0.03')

        elif self.interes == 8:
            self.porcentaje_trabajador = self.capital * Decimal('0.02')
            self.porcentaje_ganancia = self.capital * Decimal('0.02')
            self.porcentaje_gastos = self.capital * Decimal('0.01')
            self.porcentaje_reinversion = self.capital * Decimal('0.03')

        elif self.interes == 9:
            self.porcentaje_trabajador = self.capital * Decimal('0.02')
            self.porcentaje_ganancia = self.capital * Decimal('0.02')
            self.porcentaje_gastos = self.capital * Decimal('0.02')
            self.porcentaje_reinversion = self.capital * Decimal('0.03')

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