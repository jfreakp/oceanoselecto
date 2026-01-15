from django.db import models
from django.contrib.auth.models import User


TIPO_CHOICES = [
<<<<<<< HEAD
    ('P', 'PREMIUM'),
    ('N', 'NORMAL'),
]


=======
    ('P','PREMIUM'),
    ('N','NORMAL'),
]



def producto_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = f"{instance.pk}.{ext}"
    else:
        filename = f"temp.{ext}"
    return f"productos/{filename}"


>>>>>>> feature-04
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
<<<<<<< HEAD
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
=======
    imagen = models.ImageField(upload_to=producto_image_upload_to, blank=True, null=True)
>>>>>>> feature-04
    # Campos de auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='productos_creados')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='productos_modificados')
<<<<<<< HEAD
    
    class Meta:
        ordering = ['-created_at']
    
=======

    class Meta:
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Si la imagen existe y el nombre no tiene el id, renombrar
        if self.imagen and self.imagen.name.startswith('productos/temp_') and self.pk:
            import os
            from django.core.files.storage import default_storage
            old_path = self.imagen.path
            ext = old_path.split('.')[-1]
            new_filename = f"productos/{self.pk}.{ext}"
            new_path = os.path.join(default_storage.location, new_filename)
            # Si ya existe una imagen con ese nombre, eliminarla
            if os.path.exists(new_path):
                os.remove(new_path)
            # Renombrar el archivo físico
            os.rename(old_path, new_path)
            # Actualizar el campo imagen y guardar de nuevo
            self.imagen.name = new_filename
            super().save(update_fields=['imagen'])

>>>>>>> feature-04
    def __str__(self):
        return self.nombre
