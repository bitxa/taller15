from django.db import models




class Edificio(models.Model):
    opciones_tipo_Edificio = (
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30,
                            choices=opciones_tipo_Edificio)

    def _str_(self):
        return "%s %s %s %s" % (self.nombre,
                                self.direccion,
                                self.ciudad,
                                self.tipo)

    def obtener_cuartos(self):
        valor = [t.num_cuartos for t in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_costosD(self):
        valor = [t.costo for t in self.departamentos.all()]
        valor = sum(valor)
        return valor


class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30)

    #Usando el método count para obtener el total de departamentos de un propietario
    @property
    def totalDepartments(self):
        return self.departamentos.count()

    
    #Usando listas compresas para obtener los nombres de los edificios
    @property
    def edificios(self):
        return [d.edificio.nombre for d in self.departamentos.all()]

    def _str_(self):
        return "%s %s %s" % (self.nombre,
                             self.apellido,
                             self.cedula,
                             self.totalDepartments)


class Departamento(models.Model):
    costo = models.FloatField()
    num_cuartos = models.IntegerField()
    propietario = models.ForeignKey(
        Propietario, on_delete=models.CASCADE, related_name="departamentos")
    edificio = models.ForeignKey(
        Edificio, on_delete=models.CASCADE, related_name="departamentos")

    def _str_(self):
        return "%s %s %d %s" % (self.nombrePropietario,
                                self.costo,
                                self.num_cuartos,
                                self.edificio)
