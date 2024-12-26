from django.contrib import admin

from .models import Socio, Plan, Membresia, Pago, Asistencia


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    '''Admin View for Socio'''

    list_display = ('socio', 'email', 'telefono',
                    'fecha_nacimiento', 'dni', 'direccion', 'activo', 'fecha_alta')
    ordering = ('apellido', 'nombre')

    def socio(self, obj):
        return f"{obj.apellido}, {obj.nombre}"


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    '''Admin View for Plan'''
    list_display = ('nombre', 'precio_plan', 'duracion_dias', 'activo')
    list_filter = ('nombre',)
    ordering = ('nombre',)

    def precio_plan(self, obj):
        return f"${obj.precio:,.2f}"


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('socio', 'monto', 'fecha_pago', 'estado')
    list_filter = ('socio',)
    ordering = ('socio',)


admin.site.register(Membresia)

admin.site.register(Asistencia)
