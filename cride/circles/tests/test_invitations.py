"""Invitations tests."""

# Django
from django.test import TestCase


# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from cride.circles.models import Circle, Invitation, Membership
from cride.users.models import User, Profile
from rest_framework.authtoken.models import Token


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


class MemberInvitationsAPITestCase(APITestCase):
    """Member invitation API test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name='Jesus',
            last_name='Herrera',
            email='jesus.herrera@copamex.com',
            username='jesusherrera',
            password='admin123',
        )
        self.profile = Profile.objects.create(user=self.user)
        self.circle = Circle.objects.create(
            name='Departamento de desarrollo',
            slug_name='desarollo_copamex',
            about='Grupo oficial de desarrollo de Copamex',
            is_verified=True,
        )
        self.membership = Membership.objects.create(
            user=self.user,
            profile=self.profile,
            circle=self.circle,
            remaining_invitations=10,
        )

        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # URL
        circle = self.circle.slug_name
        username = self.user.username
        self.url = f'/circles/{circle}/members/{username}/invitations/'

    def test_response_success(self):
        """Verify request succed."""
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_invitation_creation(self):
        """Verify invitation are  are generated if none exist previously."""
        # Invitations in DB must be 0
        self.assertEqual(Invitation.objects.count(), 0)

        # Call member invitations URL
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        # Verify new invitations were created
        invitations = Invitation.objects.filter(issued_by=self.user)
        self.assertEqual(invitations.count(), self.membership.remaining_invitations)
        for invitation in invitations:
            self.assertIn(invitation.code, request.data['invitations'])
