import pytest


@pytest.mark.order(5)
def test_delete_entity(api_client):
    response = api_client.delete(1)

    assert response.status_code == 204, f"Ожидался статус 204, но получен {response.status_code}"