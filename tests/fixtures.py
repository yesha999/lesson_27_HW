import pytest

from tests.factories import LocationFactory, UserFactory


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    location = LocationFactory.create()
    user = UserFactory.create(location=(location,))
    django_user_model.objects.create_user(username="test", password=user.password, birth_date=user.birth_date,
                                          email="test@test.test")
    response = client.post(
        "/user/token/",
        data={"username": "test", "password": user.password},
        content_type="application/json")
    return response.data['access']
