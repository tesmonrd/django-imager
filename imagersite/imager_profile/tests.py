from django.test import TestCase
from django.contrib.auth.models import User
import factory
# Create your tests here.


class UserFactory(factory.django.DjangoFactoryModel):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: "user{}@example.com".format(n))


class Profile_Test_Case(TestCase):
    """Blag."""

    def setup(self):
        self.user = UserFactory.create()
        self.user.set_password('secret')
        # stuff necessary for running code (passwords, blagh)

    def tearDown(self):
        # tears down the stuff made in setup (goes after all tests are run)
        pass
