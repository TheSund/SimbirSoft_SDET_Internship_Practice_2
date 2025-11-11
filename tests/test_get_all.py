from typing import List

from models.entity import EntityCreate


def test_get_all_entities(api_client, created_entity):
    response = api_client.get_all()

    assert response.status_code == 200, f'Ожидался статус 200, но получен {response.status_code}'

    data = response.json()['entity']
    assert isinstance(data, List), 'Ответ не является списком'
    assert len(data) > 0, 'Список сущностей пустой'

    try:
        EntityCreate(**data[0])
    except Exception as e:
        raise AssertionError(f'Структура ответа не соответствует данным: {e}')
