from typing import List

import pytest

from data.constants import (
    TITLE,
    UPDATED_VERIFIED,
    IMPORTANT_NUMBERS,
    UPDATED_ADDITIONAL_INFO,
    ADDITIONAL_NUMBER
)
from models.entity import EntityCreate

@pytest.mark.order(4)
def test_get_all_entities(api_client):
    response = api_client.get_all()

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

    data = response.json()['entity']
    assert isinstance(data, List)

    try:
        entity = EntityCreate(**data[0])
    except Exception as e:
        raise AssertionError(f'Структура ответа не соответствует данным: {e}')

    assert entity.title == TITLE, (
        f'Возвращенное название {entity.title} не соответствует ожидаемому ({TITLE})'
    )
    assert entity.verified == UPDATED_VERIFIED, (
        f'Возвращенный статус верификации {entity.verified} не соответствует ожидаемому ({UPDATED_VERIFIED})'
    )
    assert entity.important_numbers == IMPORTANT_NUMBERS, (
        f'Возвращенные важные числа {entity.important_numbers} не соответствуют ожидаемым ({IMPORTANT_NUMBERS})'
    )
    assert entity.addition.additional_info == UPDATED_ADDITIONAL_INFO, (
        f'Возвращенная доп. информация {entity.addition.additional_info} не соответствует ожидаемой ({UPDATED_ADDITIONAL_INFO})'
    )
    assert entity.addition.additional_number == ADDITIONAL_NUMBER, (
        f'Возвращенное доп. число {entity.addition.additional_number} не соответствует ожидаемому ({ADDITIONAL_NUMBER})'
    )