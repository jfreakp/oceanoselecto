from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user: User = form.save(commit=False)
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_url = request.build_absolute_uri(
                reverse('activate', kwargs={'uidb64': uid, 'token': token})
            )

            subject = 'Activa tu cuenta'
            text_body = f"Hola {user.username},\n\nActiva tu cuenta usando este enlace:\n{activation_url}\n\nSi no creaste una cuenta, ignora este correo."
            html_body = f"<p>Hola <strong>{user.username}</strong>,</p><p>Activa tu cuenta usando este enlace:</p><p><a href=\"{activation_url}\">Activar cuenta</a></p><p>Si no creaste una cuenta, ignora este correo.</p>"

            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None) or settings.EMAIL_HOST_USER
            msg = EmailMultiAlternatives(subject, text_body, from_email, [user.email])
            msg.attach_alternative(html_body, "text/html")
            msg.send(fail_silently=True)

            return render(request, 'accounts/activation_sent.html', {'email': user.email})
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'accounts/activation_success.html')
    else:
        return render(request, 'accounts/activation_invalid.html')
