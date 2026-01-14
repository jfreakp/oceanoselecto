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

## Variables de entorno (dev/prod)
- **ENV**: `dev` | `prod` — Controla el modo por defecto.
	- Si no estableces `DEBUG`, se usa `DEBUG = (ENV != 'prod')`.
	- En `prod` se aplican valores seguros por defecto: `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, y `SOCIAL_AUTH_REDIRECT_IS_HTTPS=true`.
- **DATABASE_URL**: Cadena de conexión Postgres (ej. Supabase) `postgres://USER:PASS@HOST:PORT/DB?sslmode=require`.
	- Alternativamente: `SUPABASE_DB_URL`.
	- Si no hay `DATABASE_URL` y defines `DB_HOST/DB_NAME/DB_USER/DB_PASSWORD/DB_PORT`, se usa Postgres.
	- Si no hay nada, se usa SQLite local.
- **ALLOWED_HOSTS** y **CSRF_TRUSTED_ORIGINS**: puedes sobreescribir los defaults con listas separadas por comas.

### Ejemplo `.env` (desarrollo)
```
ENV=dev
DEBUG=true

# Para usar SQLite, no pongas DATABASE_URL
# Para Postgres local:
# DB_HOST=localhost
# DB_NAME=oceanoselecto
# DB_USER=postgres
# DB_PASSWORD=postgres
# DB_PORT=5432
```

### Vercel (producción)
- En Project Settings → Environment Variables:
	- `ENV=prod`
	- `DATABASE_URL=postgres://USER:PASS@HOST:PORT/DB?sslmode=require`
	- Opcional: `ALLOWED_HOSTS=your-domain.com,.vercel.app`
	- Opcional: `CSRF_TRUSTED_ORIGINS=https://your-domain.com,https://*.vercel.app`
