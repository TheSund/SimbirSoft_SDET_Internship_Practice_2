import allure

from api.api_client import ApiClient
from data.generators import generate_entity_data
from models.entity import Addition, EntityCreate


@allure.parent_suite('API Service Testing')
@allure.suite('Entity List Testing')
@allure.title('Creating an entity')
def test_create_entity(api_client: ApiClient) -> None:
    data = generate_entity_data()

    addition = Addition(
        additional_info=data["addition"]["additional_info"],
        additional_number=data["addition"]["additional_number"],
    )
    new_entity = EntityCreate(
        title=data["title"],
        verified=data["verified"],
        important_numbers=data["important_numbers"],
        addition=addition,
    )

    response = api_client.create(new_entity.build())

    with allure.step('Проверка успешного создания сущности'):
        assert response.status_code == 200, f'Ожидался статус 200, но получен {response.status_code}'
        response_data = response.json()
        assert isinstance(response_data, int), f'Ответ {response_data} не является ID сущности'
