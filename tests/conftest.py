from pytest_factoryboy import register

from tests.factories import UserFactory, AdFactory, CatFactory, LocationFactory

pytest_plugins = "tests.fixtures"
register(UserFactory)
register(AdFactory)
register(CatFactory)
register(LocationFactory)

