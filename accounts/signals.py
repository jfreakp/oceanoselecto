import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def ensure_default_superuser(sender, **kwargs):
    """Create a default superuser if none exists, using env vars.
    Runs after migrations for any app.
    """
    username = os.getenv("DEFAULT_SUPERUSER_USERNAME")
    email = os.getenv("DEFAULT_SUPERUSER_EMAIL")
    password = os.getenv("DEFAULT_SUPERUSER_PASSWORD")

    # Only proceed if vars exist
    if not (username and email and password):
        return

    try:
        # If any superuser exists, skip
        if User.objects.filter(is_superuser=True).exists():
            return
        # If user with username exists, ensure it's superuser/staff
        user = User.objects.filter(username=username).first()
        if user:
            if not user.is_superuser or not user.is_staff:
                user.is_superuser = True
                user.is_staff = True
                user.is_active = True
                user.save(update_fields=["is_superuser", "is_staff", "is_active"])
            return
        # Create default superuser
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
    except Exception:
        # Fail silently to avoid breaking migrations in production
        pass
