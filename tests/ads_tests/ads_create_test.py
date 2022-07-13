import pytest

from ads.serializers import AdCreateSerializer
from tests.factories import AdFactory


# @pytest.mark.parametrize("")
@pytest.mark.django_db
def test_ad_create(client, access_token):
    ad = AdFactory.create()
    data = {"name": "test ad name",
            # "author": access_token.user,
            "price": 10000,
            "description": "test description",
            "is_published": False,
            "category": ad.category.pk
            }

    expected_response = AdCreateSerializer(AdFactory.create()).data

    response = client.post("/ad/post/", data=data, content_type="application/json",
                           **{'HTTP_AUTHORIZATION': f"Bearer {access_token}"})

    assert response.status_code == 201
    # assert response.data == expected_response
