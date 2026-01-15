from django.db import models
from django.contrib.auth.models import User


TIPO_CHOICES = [
    ('P', 'PREMIUM'),
    ('N', 'NORMAL'),
]


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='productos_creados')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='productos_modificados')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.nombre
