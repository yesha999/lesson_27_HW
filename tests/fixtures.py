import pytest

from tests.factories import UserFactory, LocationFactory


@pytest.fixture
@pytest.mark.django_db
def access_token(client):
    location = LocationFactory.create()
    user = UserFactory.create(location=(location,))
    response = client.post(
        "/user/token/",
        data={"username": user.username, "password": user.password},
        content_type="application/json"
    )
    print(response.data)
    return response.data['access']
