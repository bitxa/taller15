from rest_framework import serializers
from app.models import Edificio, Departamento, Propietario


class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class PropietarioSerializer(serializers.ModelSerializer):
    departamentos = serializers.SerializerMethodField()
    edificios = serializers.SerializerMethodField()

    class Meta:
        model = Propietario
        fields = '__all__'

    def get_departamentos(self, obj):
        return obj.totalDepartments

    def get_edificios(self, obj):
        return obj.edificios
