from typing import Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


UserModel = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """Authenticate against either username or email (case-insensitive for email)."""

    def authenticate(self, request, username: Optional[str] = None, password: Optional[str] = None, **kwargs):
        if username is None or password is None:
            return None

        user = None
        # Try by username first
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            # Fallback: try by email (case-insensitive)
            try:
                user = UserModel.objects.get(email__iexact=username)
            except UserModel.DoesNotExist:
                user = None

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None