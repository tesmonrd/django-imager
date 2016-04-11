from django.test import TestCase
from .models import Photo, Album
import factory
# Create your tests here.


class UserFactory(factory.django.DjangoFactoryModel):
    class Meta:
        model = Photo, Album

class ImagesTestCase(TestCase):
    """Test the Images model."""

    def setup(self):
        self.user = UserFactory.create()
        # stuff necessary for running code (passwords, blagh)

    def tearDown(self):
        # tears down the stuff made in setup (goes after all tests are run)
        pass
