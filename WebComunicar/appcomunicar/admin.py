from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=("zona","nombres", "apellidos")
    search_fields=("zona","nombres", "apellidos") 

admin.site.register(Cliente, ClienteAdmin)