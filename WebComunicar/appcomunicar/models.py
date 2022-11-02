from django.db import models
from .choices import zonas, options
# Create your models here.

class Cliente(models.Model):
    
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.IntegerField()
    zona = models.CharField(max_length=15, choices=zonas, default='---')
    estado = models.CharField(max_length=10, choices=options, default='---')

    class Meta:
        ordering = ["nombres"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.nombres, self.estado