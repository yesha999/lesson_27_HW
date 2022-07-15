import jwt
import pytest

from lesson_27_homework.settings import SECRET_KEY
from tests.factories import AdFactory, CatFactory


@pytest.mark.django_db
def test_selection_create_not_auth(client):
    ad = AdFactory.create_batch(10)
    data = {"name": "test подборка",
            "items": [ad[0].pk, ad[3].pk, ad[7].pk]
            }

    response = client.post("/selection/post/", data=data, content_type="application/json")

    assert response.status_code == 401


@pytest.mark.django_db
def test_selection_create(client, access_token):
    ad = AdFactory.create_batch(10)
    user_id = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])['user_id']
    data = {"name": "test подборка",
            "items": [ad[0].pk, ad[3].pk, ad[7].pk]
            }

    expected_response = {"id": 1,
                         "name": "test подборка",
                         "items": [ad[0].pk, ad[3].pk, ad[7].pk],
                         "owner": user_id}

    response = client.post("/selection/post/", data=data, content_type="application/json",
                           **{'HTTP_AUTHORIZATION': f"Bearer {access_token}"})

    assert response.status_code == 201
    assert response.data == expected_response
