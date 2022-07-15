import pytest

from ads.serializers import AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_get_ads_detail_not_auth(client):
    ad = AdFactory.create()
    response = client.get(f"/ad/{ad.pk}/", content_type="application/json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_ads_detail(client, access_token):
    ad = AdFactory.create()
    response = client.get(f"/ad/{ad.pk}/", content_type="application/json",
                          **{'HTTP_AUTHORIZATION': f"Bearer {access_token}"})
    expected_response = AdDetailSerializer(ad).data
    assert response.status_code == 200
    assert response.data == expected_response
