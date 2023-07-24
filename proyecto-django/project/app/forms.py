from django.forms import ModelChoiceField, ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from app.models import *


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _("Ingrese el nombre"),
            'direccion': _("Ingrese la direccion"),
            'ciudad': _("Ingrese la ciudad"),
            'tipo': _("Elija el tipo"),
        }

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        n_ciudad = valor[0:1]
        if n_ciudad == "L":
            raise forms.ValidationError("La ciudad no puede iniciar con L")
        return valor


class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'cedula']
        labels = {
            'nombre': _("Ingrese el nombre"),
            'apellido': _("Ingrese el apellido"),
            'cedula': _("Ingrese la cedula"),
        }

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if len(valor) != 10:
            raise forms.ValidationError("La cedula debe tener 10 digitos")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'num_cuartos', 'edificio']
        labels = {
            'propietario': _("Ingrese el nombre del propietario"),
            'costo': _("Ingrese el costo"),
            'num_cuartos': _("Ingrese el número de cuartos"),
            'edificio': _("Elija el edificio"),
        }

    propietario = ModelChoiceField(
        queryset=Propietario.objects.all(), label=_("Propietario"))

    def clean_propietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())
        if num_palabras < 3:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El costo es demaciado")
        return valor

    def clean_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError(
                "El numero de cuartos no puede ser 0 o mayor de 7")
        return valor
