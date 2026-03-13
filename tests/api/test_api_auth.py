import pytest
import requests


@pytest.mark.api
def test_successful_login(base_url):
    """
    Тест-кейс 1: Успешный POST запрос (Логин).
    Используем встроенного админа Juice Shop.
    """
    endpoint = f"{base_url}/rest/user/login"

    # Body (тело запроса), которое мы отправляем на сервер
    payload = {
        "email": "admin@juice-sh.op",
        "password": "admin123"
    }

    # Отправляем POST запрос и передаем payload в формате json
    response = requests.post(endpoint, json=payload)

    # 1. Проверяем статус (должен быть 200 OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # 2. Проверяем, что сервер выдал нам токен авторизации (JWT)
    data = response.json()
    assert "token" in data["authentication"], "Auth token is missing in the response!"


@pytest.mark.api
def test_invalid_login_unauthorized(base_url):
    """
    Тест-кейс 2: Негативный POST запрос (Неверный пароль).
    Сервер не должен нас пустить и должен вернуть 401 ошибку.
    """
    endpoint = f"{base_url}/rest/user/login"
    payload = {
        "email": "admin@juice-sh.op",
        "password": "wrong_password_123"
    }

    response = requests.post(endpoint, json=payload)

    # Ожидаем статус 401 (Unauthorized)
    assert response.status_code == 401, f"Expected 401 Unauthorized, got {response.status_code}"