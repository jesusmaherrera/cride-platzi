"""Celery tasks."""

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

# Models
from cride.users.models import User

# Celery
from celery.decorators import task

# utilities
import jwt
import time
from datetime import timedelta


def gen_verification_token(user):
    """Create JWT token that the user can use to vertify its acount."""
    exp_date = timezone.now() + timedelta(days=1)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation',
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
        """Send account verification link to given user."""
        for i in range(30):
            time.sleep(1)
            print('Slieeping', str(i + 1))
        user = User.objects.get(pk=user_pk)
        verification_token = gen_verification_token(user)
        subject = (
            'Welcome @ {}! Verify your account to start using '
            'Comparte Ride').format(user.username)
        from_email = 'Comparte Ride <noreplay@comparteride.com>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {'token': verification_token, 'user': user, },
        )
        msg = EmailMultiAlternatives(
            subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
