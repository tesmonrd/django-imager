from django.conf import settings
from django.test import TestCase
from .models import Photo, Album
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
    class Meta:
        model = settings.AUTH_USER_MODEL


class ImagesAlbumsTestCase(TestCase):
    """Test the Images model."""

    def setUp(self):
        """Setup photo instance."""
        # import pdb; pdb.set_trace()
        self.user = UserFactory.create(
            username='testuser',
            email='meh@mer.gov',
            password='secret'
        )
        self.photo = PhotoFactory.create(
            photographer=self.user,
            image_title="Help",
            image_description="haaaaaaaaaaalp",
        )

        self.album = AlbumFactory.create(
            photographer=self.user,
            album_title="Its getting late",
            album_description='So go to bed already',
        )

    def test_exists(self):
        """Test if factory instance is made."""
        self.assertTrue(bool(self.photo))

    def test_image_username(self):
        """Test username."""
        self.assertIs(self.photo.photographer, self.user)

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

    def test_album_image_photographer(self):
        """Test album owner is same as photographer."""
        self.assertEqual(self.album.photographer, self.photo.photographer)

    def test_album_title(self):
        """Test album title."""
        self.assertEqual(self.album.album_title, "Its getting late")
        self.assertIsNot(self.album.album_title, "I'm feeling refreshed")

    def test_album_description(self):
        """Test album description."""
        self.assertEqual(self.album.album_description, 'So go to bed already')
        self.assertIsNot(self.album.album_description, "I'll stay up longer")

    def tearDown(self):
        """Tear down the stuff made in setup/need to make work."""
        pass
