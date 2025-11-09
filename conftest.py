import pytest
import psycopg2

from api.api_client import ApiClient
from data.data_api import BASE_URL

@pytest.fixture()
def api_client():
    return ApiClient(base_url=BASE_URL)

@pytest.fixture(scope="session", autouse=True)
def cleanup_db():
    conn = psycopg2.connect(
        dbname="test",
        user="test",
        password="test",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    conn.autocommit = True

    cursor.execute("TRUNCATE TABLE additions, entities RESTART IDENTITY CASCADE;")

    cursor.close()
    conn.close()