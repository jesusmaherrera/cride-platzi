"""User serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from cride.users.models import User, Profile


class UserModelSerializer(serializers.ModelSerializer):
    """User model serialzier."""

    class Meta:
        """Meta class."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )


class UserSignUpSerializer(serializers.Serializer):
    """User signup serializer.

    Handle signup data validation and user/profile creation.
    """

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format +99999999.'
                ' Up to 15 digits allowed.'
    )
    phone_number = serializers.CharField(
        validators=[phone_regex, ],
        max_length=17,
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=1, max_length=30)
    last_name = serializers.CharField(min_length=1, max_length=30)

    def validate(self, data):
        """Verifiy passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Password don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop("password_confirmation")
        user = User.objects.create_user(**data, is_verified=False)
        profile = Profile.objects.create(user=user)
        self.send_confirmation_email(user)
        return user, profile

    def send_confirmation_email(self, user):
        """ Send acount verification link to given user."""
        verification_token = self.get_verification_token(user)
        subject = 'Welcome @{}! Verify your acount to start using Comparte Ride'.format(user.username)
        from_email = 'Comparte Ride <noreplay@comparteride.com>'
        content = render_to_string('emails/users/account_verification.html', 
            {'token': verification_token, 'user':user, }
        )
        text_context = 'This is an important message.'
        html_context = '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, 'text/html')
        msg.send()

    def get_verification_token(self, user):
        """Create JWT token that the user can use to verify its account."""
        return 'abc'


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credientials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credientials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet :(')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""

        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
