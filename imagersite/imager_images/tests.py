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


class ImagesTestCase(TestCase):
    """Test the Images model."""

    def setUp(self):
        """Setup photo instance."""
        # import pdb; pdb.set_trace()
        self.user = UserFactory.create(
            username='testuser',
            email='death@dead.gov',
        )
        self.photo = PhotoFactory.create(
            photographer=self.user,
            image_title="Help",
            image_description="haaaaaaaaaaalp",
            published="Public",
        )

    def test_exists(self):
        """Test if factory instance is made."""
        self.assertTrue(bool(self.photo))

    def test_username(self):
        self.assertEqual(self.photo.photographer, 'testuser')


    # def tearDown(self):
    #     # tears down the stuff made in setup (goes after all tests are run)
    #     pass
