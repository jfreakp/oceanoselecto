from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio_compra', 'precio_venta', 'created_at', 'created_by')
    list_filter = ('tipo', 'created_at')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    
    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion', 'tipo', 'imagen')
        }),
        ('Precios', {
            'fields': ('precio_compra', 'precio_venta')
        }),
        ('Auditoría', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Si es un nuevo objeto
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
