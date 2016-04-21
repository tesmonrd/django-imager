from django.conf import settings
from django.test import TestCase
from django.test import Client
import unittest
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for User."""

    class Meta:
        model = settings.AUTH_USER_MODEL


class ProfileTestCase(TestCase):
    """Class for testing profile."""

    def setUp(self):
        """Setup test subject."""
        self.user = UserFactory.create(
            username='frand',
            email='happy@example.com',
            password='secret'
        )
        self.user.save()
        self.profile = self.user.profile
        self.profile.camera = 'Polaroid'
        self.profile.picture_subject = 'Grazing sheepz'
        self.profile.location = "Code Fellows' non-existent kitchen"
        self.profile.save()

    def test_user(self):
        """Test user."""
        self.assertIs(self.user.username, 'frand')
        self.assertTrue(bool(self.user.email))
        self.assertIs(self.user.password, 'secret')

    def test_camera(self):
        """Test camera."""
        self.assertIs(self.profile.camera, 'Polaroid')
        self.assertIsNot(self.profile.camera, 'Hame')

    def test_subject(self):
        """Test subject."""
        self.assertTrue(self.profile.picture_subject, 'Grazing sheepz')
        self.assertIsNot(self.profile.picture_subject, 'Dumb')

    def test_ownership(self):
        """Test profile is same as user."""
        self.assertEqual(self.profile.user, self.user)

    def test_location(self):
        """Test location."""
        self.assertTrue(self.profile.location,
                        "Code Fellows' non-existent kitchen"
                        )
        self.assertIsNot(self.profile.location, "Happily asleep")

    def tearDown(self):
        """Tear down the stuff made in setup/need to make work."""
        pass


class HttpTests(unittest.TestCase):
    """Test url routes."""

    def setUp(self):
        """Set up client."""
        self.client = Client()

    def test_home(self):
        """Test home exist."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_security(self):
        """Test csrf security on register."""
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 301)

    def test_login_security(self):
        """Test csrf security on login."""
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301)

    def test_logout_security(self):
        """Test existence on security."""
        response = self.client.get('/accounts/logout')
        self.assertEqual(response.status_code, 301)

    def test_error(self):
        """Test client reliability requests."""
        response = self.client.get('/potato')
        self.assertEqual(response.status_code, 404)
