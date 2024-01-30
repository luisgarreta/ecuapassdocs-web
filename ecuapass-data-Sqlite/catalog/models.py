from django.db import models

from django.urls import reverse  # To generate URLS by reversing URL patterns

from .models_DocCartaporte import Empresa, Cartaporte, CartaporteDoc
from .models_DocManifiesto import Conductor, Vehiculo, Manifiesto, ManifiestoDoc

#class Empresa(models.Model):
#    id = models.CharField(max_length=100, primary_key=True)
#    tipoId = models.CharField(max_length=100)
#    nombre = models.CharField(max_length=100)
#    direccion = models.CharField(max_length=100)
#    ciudad = models.CharField(max_length=100)
#    pais = models.CharField(max_length=100)
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular genre instance."""
#        return reverse('empresa-detail', args=[str(self.id)])
#
#    def __str__(self):
#        return f"{self.nombre}, {self.ciudad}"

#class Conductor(models.Model):
#    documento = models.CharField(max_length=100, primary_key=True)
#    nombre = models.CharField(max_length=100)
#    nacionalidad = models.CharField(max_length=100)
#    licencia = models.CharField(max_length=100)
#    fecha_nacimiento = models.CharField(max_length=100)
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular language instance."""
#        return reverse('conductor-detail', args=[str(self.documento)])
#
#    def __str__(self):
#        return self.documento
#
#class Vehiculo(models.Model):
#    placa = models.CharField(max_length=100, primary_key=True)
#    pais = models.CharField(max_length=100)
#    marca = models.CharField(max_length=100)
#    chasis = models.CharField(max_length=100)
#    fabricacion = models.CharField(max_length=100)
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular language instance."""
#        return reverse('vehiculo-detail', args=[str(self.placa)])
#
#    def __str__(self):
#        return self.placa

#class Cartaporte(models.Model):
#    numero = models.CharField(max_length=100, primary_key=True)
#    tipo = models.CharField(max_length=100)
#    remitente = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, related_name='cartaportes_remitente')
#    destinatario = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, related_name='cartaportes_destinatario')
#    fecha_emision = models.CharField(max_length=100)
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular language instance."""
#        return reverse('cartaporte-detail', args=[str(self.numero)])
#
#    def __str__(self):
#        return self.numero

#class Manifiesto(models.Model):
#    numero = models.CharField(max_length=100, primary_key=True)
#    tipo = models.CharField(max_length=100)
#    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True)
#    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True)
#    cartaporte = models.ForeignKey(Cartaporte, on_delete=models.RESTRICT, null=True)
#    fecha_emision = models.CharField(max_length=100)
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular language instance."""
#        return reverse('manifiesto-detail', args=[str(self.numero)])
#
#    def __str__(self):
#        return self.numero
