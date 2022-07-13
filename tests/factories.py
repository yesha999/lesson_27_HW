import factory.django

from ads.models import Ad, Category
from users.models import User, Location


class CatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Sequence(lambda n: "slug %s" % n)
    name = "test name"


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = "test name"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username%s" % n)
    password = "test"
    birth_date = "2010-12-12"
    email = factory.Sequence(lambda n: "%s@test.test" % n)

    @factory.post_generation
    def location(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for loc in extracted:
                self.location.add(loc)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test name"
    author = factory.SubFactory(UserFactory)
    price = 10000
    description = "test description"
    is_published = False
    category = factory.SubFactory(CatFactory)
