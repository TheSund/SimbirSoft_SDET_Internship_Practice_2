import psycopg2
import pytest

from api.api_client import ApiClient
from data.data_api import BASE_URL
from data.generators import generate_entity_data
from models.entity import Addition, EntityCreate


@pytest.fixture(scope='function')
def api_client():
    return ApiClient(base_url=BASE_URL)


@pytest.fixture(scope='function')
def created_entity(api_client):
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

    create_resp = api_client.create(new_entity.build())
    assert create_resp.status_code == 200, f"Ошибка создания: {create_resp.status_code}"
    entity_id = create_resp.json()

    yield entity_id, data

    delete_resp = api_client.delete(entity_id)
    if delete_resp.status_code not in (204, 500):
        raise AssertionError(f"Ошибка при удалении: {delete_resp.status_code}")


def pytest_configure():
    print("\n>>> Очистка базы данных перед тестами <<<")
    conn = psycopg2.connect(
        dbname="test",
        user="test",
        password="test",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE additions, entities RESTART IDENTITY CASCADE;")
    conn.close()


def pytest_unconfigure():
    print("\n>>> Очистка базы после тестов <<<")
    conn = psycopg2.connect(
        dbname="test",
        user="test",
        password="test",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE additions, entities RESTART IDENTITY CASCADE;")
    conn.close()
