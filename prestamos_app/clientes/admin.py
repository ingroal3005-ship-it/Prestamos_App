from django.contrib import admin
from .models import Cliente, Pago
from django.db.models import Sum
from django.utils.formats import number_format

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'capital',
        'total',
        'trabajador',
        'ganancia',
        'mostrar_gastos',
        'reinversion',
    )

    readonly_fields = (
        'porcentaje_total',
        'porcentaje_trabajador',
        'porcentaje_ganancia',
        'porcentaje_gastos',
        'porcentaje_reinversion',
    )

    # 🔹 Formato $
    def formatear_moneda(self, valor):
        if valor is None:
            return "$0.00"
        return f"${number_format(valor, decimal_pos=2, use_l10n=True)}"

    def capital(self, obj):
        return self.formatear_moneda(obj.capital)

    def total(self, obj):
        return self.formatear_moneda(obj.porcentaje_total)

    def trabajador(self, obj):
        return self.formatear_moneda(obj.porcentaje_trabajador)

    def ganancia(self, obj):
        return self.formatear_moneda(obj.porcentaje_ganancia)

    def reinversion(self, obj):
        return self.formatear_moneda(obj.porcentaje_reinversion)

    def mostrar_gastos(self, obj):
        if obj.interes == 7:
            return "No aplica"
        return self.formatear_moneda(obj.porcentaje_gastos)

    mostrar_gastos.short_description = "Gastos y Sueldos"


admin.site.register(Pago)