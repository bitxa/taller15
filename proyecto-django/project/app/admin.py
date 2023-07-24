from django.contrib import admin

from app.models import *


class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'costo', 'num_cuartos', 'edificio')
    raw_id_fields = ('propietario', 'edificio')
    
admin.site.register(Departamento, DepartamentoAdmin)

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'totalDepartments', 'edificios' )
    search_fields = ('nombre', 'apellido')


admin.site.register(Propietario, PropietarioAdmin)
