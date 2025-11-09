import pytest

from data.constants import (
    TITLE,
    UPDATED_VERIFIED,
    IMPORTANT_NUMBERS,
    UPDATED_ADDITIONAL_INFO,
    ADDITIONAL_NUMBER
)
from models.entity import Addition, EntityCreate

@pytest.mark.order(3)
def test_patch_entity(api_client):
    addition_obj = Addition(
        additional_info = UPDATED_ADDITIONAL_INFO,
        additional_number = ADDITIONAL_NUMBER
    )

    updated_data = EntityCreate(
        title = TITLE,
        verified = UPDATED_VERIFIED,
        important_numbers = IMPORTANT_NUMBERS,
        addition = addition_obj
    )
    response = api_client.patch(1, data=updated_data.build())

    assert response.status_code == 204, f"Ожидался статус 204, но получен {response.status_code}"