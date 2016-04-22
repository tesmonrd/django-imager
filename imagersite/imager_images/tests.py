from django.conf import settings
from django.test import TestCase
from .models import Photo, Album
from django.test import Client
import unittest
import factory
# Create your tests here.


class PhotoFactory(factory.django.DjangoModelFactory):
    """Target the model for the factory."""

    class Meta:
        model = Photo


class AlbumFactory(factory.django.DjangoModelFactory):
    """Target the model for the factory."""

    class Meta:
        model = Album


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for User."""

    class Meta:
        model = settings.AUTH_USER_MODEL


class ImagesAlbumsTestCase(TestCase):
    """Test the Images model."""

    def setUp(self):
        """Setup photo instance."""
        self.user = UserFactory.create(
            username='testuser',
            email='meh@mer.gov',
            password='secret'
        )
        self.photo = PhotoFactory.create(
            user=self.user,
            image_title="Help",
            image_description="haaaaaaaaaaalp",
            published='Public'
        )

        self.album = AlbumFactory.create(
            user=self.user,
            album_title="Its getting late",
            album_description='So go to bed already',
            published='Private'
        )

    def test_exists(self):
        """Test if factory instance is made."""
        self.assertTrue(bool(self.photo))

    def test_image_username(self):
        """Test username."""
        self.assertIs(self.photo.user, self.user)

    def test_image_title(self):
        """Test image title."""
        self.assertEqual(self.photo.image_title, 'Help')

    def test_description(self):
        """Test image description."""
        self.assertEqual(self.photo.image_description, 'haaaaaaaaaaalp')

    def test_user(self):
        """Test user properties."""
        self.assertTrue(bool(self.user.username))
        self.assertTrue(bool(self.user.email))
        self.assertTrue(bool(self.user.password))

    def test_default_publish(self):
        """Test default publish settings."""
        self.assertIs(self.photo.published, 'Public')

    def test_album_exists(self):
        """Test album exists."""
        self.assertTrue(self.album)

    def test_album_image_user(self):
        """Test album owner is same as user."""
        self.assertEqual(self.album.user, self.photo.user)

    def test_album_title(self):
        """Test album title."""
        self.assertEqual(self.album.album_title, "Its getting late")
        self.assertIsNot(self.album.album_title, "I'm feeling refreshed")

    def test_album_description(self):
        """Test album description."""
        self.assertEqual(self.album.album_description, 'So go to bed already')
        self.assertIsNot(self.album.album_description, "I'll stay up longer")

    def test_published(self):
        """Test pushed status."""
        self.assertEqual(self.photo.published, 'Public')
        self.assertEqual(self.album.published, 'Private')

    def tearDown(self):
        """Tear down the stuff made in setup/need to make work."""
        pass


class HttpTests(unittest.TestCase):
    """Test url routes."""

    def setUp(self):
        """Set up client."""
        self.client = Client()

    def test_secure_library(self):
        """Test library view is secured."""
        response = self.client.get('/library/')
        self.assertEqual(response.status_code, 302)

    def test_profile_secure_login(self):
        """Test profile is secure."""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)

    def test_images_add(self):
        """Test image add view exists."""
        response = self.client.get('/images/photos/add')
        self.assertEqual(response.status_code, 200)
