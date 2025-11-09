import pytest

from data.constants import (
    TITLE,
    VERIFIED,
    IMPORTANT_NUMBERS,
    ADDITIONAL_INFO,
    ADDITIONAL_NUMBER
)
from models.entity import Entity


@pytest.mark.order(2)
def test_get_entity(api_client):
    response = api_client.get(1)

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

    try:
        parsed = Entity(**response.json())
    except Exception as e:
        raise AssertionError(f'Структура ответа не соответствует данным: {e}')

    assert parsed.title == TITLE, (
        f'Возвращенное название {parsed.title} не соответствует ожидаемому ({TITLE})'
    )
    assert parsed.verified == VERIFIED, (
        f'Возвращенный статус верификации {parsed.verified} не соответствует ожидаемому ({VERIFIED})'
    )
    assert parsed.important_numbers == IMPORTANT_NUMBERS, (
        f'Возвращенные важные числа {parsed.important_numbers} не соответствуют ожидаемым ({IMPORTANT_NUMBERS})'
    )
    assert parsed.addition.additional_info == ADDITIONAL_INFO, (
        f'Возвращенная доп. информация {parsed.addition.additional_info} не соответствует ожидаемой ({ADDITIONAL_INFO})'
    )
    assert parsed.addition.additional_number == ADDITIONAL_NUMBER, (
        f'Возвращенное доп. число {parsed.addition.additional_number} не соответствует ожидаемому ({ADDITIONAL_NUMBER})'
    )