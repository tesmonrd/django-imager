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


# class ImagesTestCase(TestCase):
#     """Test the Images model."""

#     def setUp(self):
#         """Setup photo instance."""
#         # import pdb; pdb.set_trace()
#         self.photo = PhotoFactory.create(
#             photographer=self.User,
#             image_title="Help",
#             image_description="haaaaaaaaaaalp",
#             published="Public",
#         )


#     def test_exists(self):
#         """Test if factory instance is made."""
#         self.assertTrue(self.photo)


    # def tearDown(self):
    #     # tears down the stuff made in setup (goes after all tests are run)
    #     pass
