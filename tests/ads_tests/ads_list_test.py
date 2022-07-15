import pytest

from ads.serializers import AdListSerializer
from lesson_27_homework.settings import REST_FRAMEWORK
from tests.factories import AdFactory


@pytest.mark.django_db
def test_get_ads_list(client):
    TOTAL_LIST_SIZE = 9
    ads = AdFactory.create_batch(TOTAL_LIST_SIZE)
    response = client.get("/ad/", content_type="application/json")
    expected_response = AdListSerializer(ads, many=True).data[:REST_FRAMEWORK["PAGE_SIZE"]]
    print(response.data)
    assert response.status_code == 200
    assert response.data['results'] == expected_response
    assert response.data['count'] == TOTAL_LIST_SIZE
