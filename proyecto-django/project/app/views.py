from django.shortcuts import render, redirect
from app.forms import EdificioForm, DepartamentoForm, PropietarioForm
from app.models import Edificio, Departamento, Propietario
from rest_framework import viewsets, permissions
from .serializers import EdificioSerializer, DepartamentoSerializer, PropietarioSerializer


def index(request):
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios}
    return render(request, 'index.html', informacion_template)


def crear_edificio(request):
    if request.method == 'POST':
        formulario = EdificioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crearEdificio.html', diccionario)


def crear_departamento(request):
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crearDepartamento.html', diccionario)


def crear_propietario(request):
    if request.method == 'POST':
        formulario = PropietarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = PropietarioForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crearPropietario.html', diccionario)


def editar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}
    return render(request, 'editarEdificio.html', diccionario)


def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect('index')


def editar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}
    return render(request, 'editarDepartamento.html', diccionario)


def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect('index')


def editar_propietario(request, id):
    propietario = Propietario.objects.get(pk=id)
    if request.method == 'POST':
        formulario = PropietarioForm(request.POST, instance=propietario)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = PropietarioForm(instance=propietario)
    diccionario = {'formulario': formulario}
    return render(request, 'editarPropietario.html', diccionario)


def eliminar_propietario(request, id):
    propietario = Propietario.objects.get(pk=id)
    propietario.delete()
    return redirect('index')


def obtener_edificios(request, id):
    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificios': edificio}
    return render(request, 'listado_edificio.html', informacion_template)


def obtener_departamentos(request, id):
    departamento = Departamento.objects.get(pk=id)
    informacion_template = {'departamentos': departamento}
    return render(request, 'listado_departamento.html', informacion_template)


def obtener_propietarios(request, id):
    propietario = Propietario.objects.get(pk=id)
    informacion_template = {'propietarios': propietario}
    return render(request, 'listado_propietario.html', informacion_template)


class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [permissions.IsAuthenticated]
