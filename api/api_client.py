import requests

from data.data_api import (
    CREATE,
    DELETE,
    GET,
    GET_ALL,
    PATCH
)


class ApiClient:
    """Класс для взаимодействия с API. Осуществляет основные HTTP-запросы с сущностями:
    создание сущности, удаление, получение, получение списка сущностей и обновление сущности."""
    def __init__(self, base_url):
        """Инициализация клиента API с базовым URL."""
        self.base_url = base_url

    def create(self, data: dict, **kwargs) -> requests.Response:
        """Отправляет POST запрос для создания новой сущности."""
        return requests.post(f"{self.base_url}{CREATE}", json=data, **kwargs)

    def delete(self, entity_id: int, **kwargs) -> requests.Response:
        """Отправляет DELETE запрос для удаления сущности по ID."""
        return requests.delete(f"{self.base_url}{DELETE}{entity_id}", **kwargs)

    def get(self, entity_id: int, **kwargs) -> requests.Response:
        """Отправляет GET запрос для получения данных сущности по ID."""
        return requests.get(f"{self.base_url}{GET}{entity_id}", **kwargs)

    def get_all(self, **kwargs) -> requests.Response:
        """Отправляет GET запрос для получения списка всех сущностей."""
        return requests.get(f"{self.base_url}{GET_ALL}", **kwargs)

    def patch(self, entity_id: int, data: dict, **kwargs) -> requests.Response:
        """Отправляет GET запрос для получения данных сущности по ID."""
        return requests.patch(f"{self.base_url}{PATCH}{entity_id}", json=data, **kwargs)
