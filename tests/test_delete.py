def test_delete_entity(api_client, created_entity):
    entity_id, _ = created_entity
    response = api_client.delete(entity_id)
    assert response.status_code == 204, f"Ожидался статус 204, но получен {response.status_code}"

    response = api_client.get(entity_id)
    assert response.status_code == 500, f"Ожидался статус 500, но получен {response.status_code}"
