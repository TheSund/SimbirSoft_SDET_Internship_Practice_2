from typing import List

import allure

from models.entity import EntityCreate


@allure.parent_suite('API Service Testing')
@allure.suite('Entity List Testing')
@allure.title('Getting entity list')
def test_get_all_entities(api_client, created_entity):
    response = api_client.get_all()

    with allure.step('Проверка успешного получения списка сущностей'):
        assert response.status_code == 200, f'Ожидался статус 200, но получен {response.status_code}'

    with allure.step('Проверка валидности списка'):
        data = response.json()['entity']
        assert isinstance(data, List), 'Ответ не является списком'
        assert len(data) > 0, 'Список сущностей пустой'

    with allure.step('Проверка соответствия сущности в списке схеме'):
        try:
            EntityCreate(**data[0])
        except Exception as e:
            raise AssertionError(f'Структура ответа не соответствует данным: {e}')
