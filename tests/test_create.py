import pytest

from data.constants import (
    TITLE,
    VERIFIED,
    IMPORTANT_NUMBERS,
    ADDITIONAL_INFO,
    ADDITIONAL_NUMBER
)
from models.entity import Addition, EntityCreate


@pytest.mark.order(1)
def test_create_entity(api_client):
    addition_obj = Addition(
        additional_info = ADDITIONAL_INFO,
        additional_number = ADDITIONAL_NUMBER
    )

    new_entity = EntityCreate(
        title = TITLE,
        verified = VERIFIED,
        important_numbers = IMPORTANT_NUMBERS,
        addition = addition_obj
    )

    response = api_client.create(data=new_entity.build())

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

    response_data = response.json()
    assert isinstance(response_data, int), f'Ответ {response_data} не является ID сущности'
