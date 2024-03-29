
import json, os, re
from os.path import join

from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

# For CSRF protection
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

# For textarea options
from django.db.models import Q

# Own imports
from .DocEcuapassView import DocEcuapassView
from shared.models import ManifiestoDoc, Manifiesto, Vehiculo, Conductor

#--------------------------------------------------------------------
#-- Vista para manejar las solicitudes de manifiesto
#--------------------------------------------------------------------
class DocManifiestoView (DocEcuapassView):
	template_name = "manifiesto-forma.html"

	def __init__(self, *args, **kwargs):
		super().__init__ ("manifiesto", "manifiesto-forma.html", "manifiesto_input_parameters.json", *args, **kwargs)

	#-------------------------------------------------------------------
	#-- Guarda los campos del documento manifiesto (incluye numero) a la BD
	#-------------------------------------------------------------------
	def saveDocumentToDB (self, inputValues, fieldValues, flagSave):
		# Create ecuapassDoc and save it to get id
		if flagSave == "GET-ID":
			# Save Manifiesto document
			ecuapassDoc = ManifiestoDoc ()
			ecuapassDoc.save ()
			ecuapassDoc.numero = self.getManifiestoNumber (ecuapassDoc.id)
			ecuapassDoc.save ()

			# Save Manifiesto register
			manifiestoReg = Manifiesto ()
			manifiestoReg.setValues (ecuapassDoc, fieldValues)
			manifiestoReg.save ()

			return ecuapassDoc.numero
		elif flagSave == "SAVE-DATA":
			# Retrieve instance and save Manifiesto document
			docNumber = inputValues ["txt00"]
			ecuapassDoc = get_object_or_404 (ManifiestoDoc, numero=docNumber)

			# Assign values to the attributes using dictionary keys
			for key, value in inputValues.items():
				setattr(ecuapassDoc, key, value)

			ecuapassDoc.save ()

			# Retrieve and save Manifiesto register
			manifiestoReg = get_object_or_404 (Manifiesto, numero=docNumber)
			manifiestoReg.setValues (ecuapassDoc, fieldValues)
			manifiestoReg.save ()

			return inputValues

	#-- Create a formated manifiesto number ranging from 2000000 
	def getManifiestoNumber (self, id):
		numero = f"CO{2000000 + id}"
		return (numero)
		
#--------------------------------------------------------------------
#-- Class for autocomplete options while the user is typing
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# Show options when user types in "input_placaPais"
#--------------------------------------------------------------------
class VehiculoOptionsView (View):
	@method_decorator(csrf_protect)
	def get (self, request, *args, **kwargs):
		query = request.GET.get('query', '')
		options = Vehiculo.objects.filter (placa__icontains=query).values()

		itemOptions = []
		for i, option in enumerate (options):
			itemLine = f"{i}. {option['placa']}"
			itemText = "%s||%s||%s. %s||%s" % (option["marca"], option["anho"], option["placa"], option ["pais"], option ["chasis"])
			newOption = {"itemLine" : itemLine, "itemText" : itemText}
			itemOptions.append (newOption)
		
		return JsonResponse (itemOptions, safe=False)

#--------------------------------------------------------------------
# Show options when user types in "input_placaPais"
#--------------------------------------------------------------------
class ConductorOptionsView (View):
	@method_decorator(csrf_protect)
	def get (self, request, *args, **kwargs):
		query = request.GET.get('query', '')
		options = Conductor.objects.filter (nombre__icontains=query).values()

		itemOptions = []
		for i, option in enumerate (options):
			itemLine = f"{i}. {option['nombre']}"
			itemText = "%s||%s||%s||%s||%s" % (option["nombre"], option["documento"], 
			           option["nacionalidad"], option ["licencia"], option ["fecha_nacimiento"])
			newOption = {"itemLine" : itemLine, "itemText" : itemText}
			itemOptions.append (newOption)
		
		return JsonResponse (itemOptions, safe=False)
