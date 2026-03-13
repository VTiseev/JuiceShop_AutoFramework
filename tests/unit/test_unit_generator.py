import pytest
from utils.data_generator import generate_random_user


@pytest.mark.unit
def test_random_user_generation():
    """
    Unit-тест 1: Проверяем, что наша утилита возвращает правильные ключи.
    """
    user = generate_random_user()

    # Проверяем, что функция вернула словарь с нужными ключами
    assert "email" in user
    assert "password" in user


@pytest.mark.unit
def test_random_user_email_format():
    """
    Unit-тест 2: Проверяем, что сгенерированный email похож на настоящий.
    """
    user = generate_random_user()
    email = user["email"]

    # Базовая проверка формата email (наличие @ и точки)
    assert "@" in email, f"Generated email '{email}' is missing '@' symbol!"
    assert "." in email, f"Generated email '{email}' is missing domain dot!"


@pytest.mark.unit
def test_random_user_password_length():
    """
    Unit-тест 3: Проверяем, что пароль соответствует заданной длине.
    """
    user = generate_random_user()
    password = user["password"]

    # Мы просили Faker сделать пароль длиной 12 символов
    assert len(password) == 12, f"Expected password length 12, but got {len(password)}"