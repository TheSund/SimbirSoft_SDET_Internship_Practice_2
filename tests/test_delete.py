import allure

from api.api_client import ApiClient


@allure.parent_suite('API Service Testing')
@allure.suite('Entity List Testing')
@allure.title('Deleting an entity')
def test_delete_entity(api_client: ApiClient, created_entity: tuple[int, dict]) -> None:
    entity_id, _ = created_entity
    response = api_client.delete(entity_id)
    with allure.step('Проверка успешности запроса на удаление'):
        assert response.status_code == 204, f'Ожидался статус 204, но получен {response.status_code}'

    with allure.step('Проверка успешного удаления сущности'):
        response = api_client.get(entity_id)
        assert response.status_code == 500, f'Ожидался статус 500, но получен {response.status_code}'
