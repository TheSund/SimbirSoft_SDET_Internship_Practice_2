from models.entity import Addition, EntityCreate


def test_patch_entity(api_client, created_entity):
    entity_id, existing_data = created_entity

    updated_verified = not existing_data["verified"]
    updated_add_info = 'ОБНОВЛЕНО'

    addition = Addition(
        additional_info=updated_add_info,
        additional_number=existing_data["addition"]["additional_number"],
    )
    updated_data = EntityCreate(
        title=existing_data["title"],
        verified=updated_verified,
        important_numbers=existing_data["important_numbers"],
        addition=addition,
    )

    response = api_client.patch(entity_id, updated_data.build())
    assert response.status_code == 204, f'Ошибка при обновлении сущности: {response.status_code}, {response.text}'
