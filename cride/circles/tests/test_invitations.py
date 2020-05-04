"""Invitations tests."""

# Django
from django.test import TestCase

# Model
from cride.circles.models import Circle, Invitation
from cride.users.models import User


class InvitationManagerTestCase(TestCase):
    """Invitation manager test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name='Jesus',
            last_name='Herrera',
            email='jesus.herrera@copamex.com',
            username='jesus.herrera',
            password='admin123',
        )
        self.circle = Circle.objects.create(
            name='Departamento de desarrollo',
            slug_name='desarollo_copamex',
            about='Grupo oficial de desarrollo de Copamex',
            is_verified=True,
        )

    def test_code_generation(self):
        """Random codes should be generated automatically."""
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
        )
        self.assertIsNotNone(invitation.code)

    def test_code_usage(self):
        """If a code is given, there's no need to createa a new code."""
        code = 'holamundo'
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
            code=code,
        )
        self.assertEqual(invitation.code, code)

    def test_code_generation_if_duplicated(self):
        """If given code is not unique, a new one must be generated."""
        code = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
        ).code

        # Create another invitation with the past code
        invitation = Invitation.objects.create(
            issued_by=self.user,
            circle=self.circle,
            code=code,
        )

        self.assertNotEqual(invitation.code, code)
