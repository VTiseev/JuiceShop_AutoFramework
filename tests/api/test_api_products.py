import pytest
import requests
from jsonschema import validate
from utils.schemas.product_schema import GET_PRODUCTS_SCHEMA

@pytest.mark.api
def test_get_all_products(base_url):
    """
    Тест-кейс: Получение списка всех товаров через API.
    Шаги:
    1. Отправить GET-запрос на эндпоинт /api/Products.
    2. Проверить, что статус-код ответа == 200.
    3. Проверить, что структура ответа (JSON) соответствует ожидаемому контракту.
    4. Убедиться, что список товаров не пустой.
    """
    # 1. Формируем полный URL и отправляем запрос
    endpoint = f"{base_url}/api/Products"
    response = requests.get(endpoint)

    # 2. Проверяем статус-код (Assert)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # 3. Преобразуем ответ в словарь Python (JSON)
    response_data = response.json()

    # 4. ВАЛИДАЦИЯ КОНТРАКТА: сверяем ответ с нашей схемой
    # Если структура не совпадет, jsonschema автоматически выбросит ошибку ValidationError
    validate(instance=response_data, schema=GET_PRODUCTS_SCHEMA)

    # 5. Дополнительная бизнес-проверка: массив товаров не должен быть пустым
    assert len(response_data["data"]) > 0, "Server returned an empty list of products!"

@pytest.mark.api
def test_get_product_by_id(base_url):
    """
    Тест-кейс 3: GET запрос с параметром пути (Path Variable).
    Проверяем получение конкретного яблочного сока (id=1).
    """
    product_id = 1
    # Добавляем ID в конец URL (например: /api/Products/1)
    endpoint = f"{base_url}/api/Products/{product_id}"

    response = requests.get(endpoint)

    # 1. Проверяем, что запрос успешен
    assert response.status_code == 200

    data = response.json()

    # 2. Проверяем, что сервер вернул именно тот ID, который мы просили
    assert data["data"]["id"] == product_id, f"Expected product ID {product_id}, but got {data['data']['id']}"