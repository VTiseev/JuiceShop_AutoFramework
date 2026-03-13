import pytest
import allure
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:3000"  # Твой локальный докер-стенд


@pytest.fixture(scope="session")
def base_url():
    """Возвращает базовый URL стенда."""
    return BASE_URL


@pytest.fixture(scope="function")
def page():
    """Фикстура для UI-тестов с автоматическим скриншотом в конце."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        # Передаем страницу в тест (здесь выполняется сам тест-кейс)
        yield page

        # ==========================================
        # 📸 POSTCONDITION: Скриншот для Allure
        # ==========================================
        # Делаем скриншот всей страницы (даже если она с прокруткой)
        screenshot_bytes = page.screenshot(full_page=True)

        # Прикрепляем байты картинки к Allure-отчету текущего теста
        allure.attach(
            screenshot_bytes,
            name="Final_Step_Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        # Закрываем браузер
        browser.close()