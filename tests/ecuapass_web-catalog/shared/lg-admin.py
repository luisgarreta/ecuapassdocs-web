from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(ManifiestoDoc)
admin.site.register(Manifiesto)
admin.site.register(Vehiculo)
admin.site.register(Conductor)

admin.site.register(CartaporteDoc)
admin.site.register(Cartaporte)
admin.site.register(Empresa)
