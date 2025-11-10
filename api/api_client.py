import requests

from data.data_api import (
    CREATE,
    DELETE,
    GET,
    GET_ALL,
    PATCH
)


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create(self, data: dict, **kwargs) -> requests.Response:
        return requests.post(f"{self.base_url}{CREATE}", json=data, **kwargs)

    def delete(self, entity_id: int, **kwargs) -> requests.Response:
        return requests.delete(f"{self.base_url}{DELETE}{entity_id}", **kwargs)

    def get(self, entity_id: int, **kwargs) -> requests.Response:
        return requests.get(f"{self.base_url}{GET}{entity_id}", **kwargs)

    def get_all(self, **kwargs) -> requests.Response:
        return requests.get(f"{self.base_url}{GET_ALL}", **kwargs)

    def patch(self, entity_id: int, data: dict, **kwargs) -> requests.Response:
        return requests.patch(f"{self.base_url}{PATCH}{entity_id}", json=data, **kwargs)