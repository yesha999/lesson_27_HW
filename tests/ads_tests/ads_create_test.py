import jwt
import pytest

from lesson_27_homework.settings import SECRET_KEY
from tests.factories import AdFactory, CatFactory


@pytest.mark.django_db
def test_ad_create(client, access_token):
    ad = AdFactory.create()  # id(pk) = 1
    user_id = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])['user_id']
    data = {"name": "test ad name",
            "author": user_id,
            "price": 10000,
            "description": "test description",
            "is_published": False,
            "category": ad.category.pk
            }

    # ожидаем id = 2, так как id = 1 создает фабрика ad
    expected_response = {'id': 2, 'is_published': False, 'name': 'test ad name', 'price': 10000,
                         'description': 'test description', 'image': None, 'author': user_id, 'category': 1}

    # Не проходит assert через сериализатор, так как фабрика на создание юзера не кладет его в базу данных,
    # в связи с этим невозможно "честно" получить author_id по токену создателя объявления, как задумано в приложении
    # expected_response_1 = AdCreateSerializer(ad).data

    response = client.post("/ad/post/", data=data, content_type="application/json",
                           **{'HTTP_AUTHORIZATION': f"Bearer {access_token}"})  # id(pk) = 2

    assert response.status_code == 201
    assert response.data == expected_response
    # assert response.data == expected_response_1 - не работает по вышеуказанным причинам


# Проверка на автоматическое присвоение автора по токену
@pytest.mark.django_db
def test_author_id_auto_create(client, access_token):
    category = CatFactory.create()
    user_id = jwt.decode(access_token, SECRET_KEY, algorithms=["HS256"])['user_id']
    data = {"name": "test ad name",
            "price": 10000,
            "description": "test description",
            "is_published": False,
            "category": category.pk
            }

    expected_response = {'id': 3, 'is_published': False, 'name': 'test ad name', 'price': 10000,
                         'description': 'test description', 'image': None, 'author': user_id, 'category': category.pk}

    response = client.post("/ad/post/", data=data, content_type="application/json",
                           **{'HTTP_AUTHORIZATION': f"Bearer {access_token}"})

    assert response.status_code == 201
    assert response.data == expected_response


# Проверка на запрет на проставление is_published True
@pytest.mark.django_db
def test_is_published_not_true(client, access_token):
    category = CatFactory.create()
    data = {"name": "test ad name",
            "price": 10000,
            "description": "test description",
            "is_published": True,
            "category": category.pk
            }

    response = client.post("/ad/post/", data=data, content_type="application/json",
                           **{'HTTP_AUTHORIZATION': f"Bearer {access_token}"})

    # Не понял с чем сделать assert
    expected_response = 'Значение поля is_published при создании объявления не может быть True.'

    assert response.status_code == 400
