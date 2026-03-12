import pytest
from playwright.sync_api import sync_playwright

# Глобальный URL нашего тестового стенда
BASE_URL = "http://localhost:3000"


@pytest.fixture(scope="session")
def base_url():
    """Возвращает базовый URL стенда."""
    return BASE_URL


@pytest.fixture(scope="function")
def page():
    """
    Фикстура для UI-тестов.
    Открывает браузер перед тестом и закрывает после (Preconditions / Postconditions).
    scope="function" означает, что для каждого теста будет новый чистый браузер.
    """
    with sync_playwright() as p:
        # Запускаем Chromium. headless=False позволяет нам видеть, как браузер кликает
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        yield page  # Передаем страницу в тест (здесь тест выполняется)

        # Postcondition: закрываем браузер после теста
        browser.close()