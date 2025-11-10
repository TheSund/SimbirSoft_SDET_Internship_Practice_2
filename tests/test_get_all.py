from typing import List

import pytest

from models.entity import EntityCreate


@pytest.mark.order(4)
def test_get_all_entities(api_client, created_entity):
    response = api_client.get_all()

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

    data = response.json()['entity']
    assert isinstance(data, List)
    assert len(data) > 0

    try:
        entity = EntityCreate(**data[0])
    except Exception as e:
        raise AssertionError(f'Структура ответа не соответствует данным: {e}')
