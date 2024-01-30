from django.contrib import admin

# Register your models here.
from .models import Empresa, Conductor, Vehiculo, Cartaporte, Manifiesto

#admin.site.register(Empresa)
#admin.site.register(Conductor)
admin.site.register(Vehiculo)
#admin.site.register(Cartaporte)
#admin.site.register(Manifiesto)

# Define the admin class
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numeroId', 'direccion', 'ciudad', 'pais')

# Register the admin class with the associated model
admin.site.register(Empresa, EmpresaAdmin)

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'nacionalidad', 'licencia')

# Register the admin class with the associated model
admin.site.register(Conductor, ConductorAdmin)

class ManifiestoInline(admin.TabularInline):
    model = Manifiesto

class CartaporteAdmin(admin.ModelAdmin):
    list_display = ('numero', 'remitente', 'fecha_emision')
    inlines = [ManifiestoInline]

admin.site.register(Cartaporte, CartaporteAdmin)

class ManifiestoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cartaporte', 'fecha_emision')

admin.site.register(Manifiesto, ManifiestoAdmin)
