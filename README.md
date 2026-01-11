# Oceanoselecto — App "home"

Esta app agrega una página de inicio simple al proyecto Django.

## Requisitos
- Python 3.10+ (recomendado 3.11)
- Django 6.0.x

## Instalación
Si aún no tienes Django instalado:

```bash
pip install "Django>=6.0,<6.1"
```

## Ejecutar el servidor
Desde la carpeta del proyecto (donde está `manage.py`):

```bash
python manage.py runserver
```

Luego abre en el navegador:
- http://127.0.0.1:8000/ → Página de inicio
- http://127.0.0.1:8000/admin/ → Admin (si tienes usuarios creados)

## Estructura creada
- [home/apps.py](home/apps.py)
- [home/views.py](home/views.py)
- [home/urls.py](home/urls.py)
- [home/templates/home/index.html](home/templates/home/index.html)
- [oceanoselecto/settings.py](oceanoselecto/settings.py) → `INSTALLED_APPS` actualizado
- [oceanoselecto/urls.py](oceanoselecto/urls.py) → incluido `home.urls`

## Personalización
- Edita la plantilla en [home/templates/home/index.html](home/templates/home/index.html) para cambiar estilos y contenido.
- Agrega más vistas y rutas en [home/urls.py](home/urls.py).
