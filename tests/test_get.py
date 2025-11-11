from models.entity import Entity


def test_get_entity(api_client, created_entity):
    entity_id, expected_data = created_entity
    response = api_client.get(entity_id)

    assert response.status_code == 200, f'Ожидался статус 200, но получен {response.status_code}'

    try:
        parsed = Entity(**response.json())
    except Exception as e:
        raise AssertionError(f'Структура ответа не соответствует данным: {e}')

    assert parsed.title == expected_data["title"], (
        f'Возвращенное название не соответствует ожидаемому. '
        f'Ожидалось: {expected_data["title"]}'
        f' получено: {parsed.title}'
    )
    assert parsed.verified == expected_data["verified"], (
        f'Возвращенный статус верификации не соответствует ожидаемому.'
        f'Ожидалось: {expected_data["verified"]},'
        f' получено: {parsed.verified}'
    )
    assert parsed.important_numbers == expected_data["important_numbers"], (
        f'Возвращенные важные числа не соответствуют ожидаемым.'
        f'Ожидалось: {expected_data["important_numbers"]},'
        f' получено: {parsed.important_numbers}'
    )
    assert parsed.addition.additional_info == expected_data["addition"]["additional_info"], (
        f'Возвращенная доп. информация не соответствует ожидаемой.'
        f'Ожидалось: {expected_data["addition"]["additional_info"]},'
        f' получено: {parsed.addition.additional_info}'
    )
    assert parsed.addition.additional_number == expected_data["addition"]["additional_number"], (
        f'Возвращенное доп. число не соответствует ожидаемому.'
        f'Ожидалось: {expected_data["addition"]["additional_number"]}, '
        f' получено: {parsed.addition.additional_number}'
    )
