import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.ui
def test_invalid_login(page, base_url):
    """
    Тест-кейс: Авторизация с неверными учетными данными.
    Шаги:
    1. Открыть главную страницу.
    2. Закрыть баннеры (Welcome и Cookie).
    3. Перейти на страницу логина (Account -> Login).
    4. Ввести неверный email и пароль.
    5. Проверить, что появилось сообщение "Invalid email or password.".
    """
    home_page = HomePage(page)
    login_page = LoginPage(page)

    # 1. Предусловия (открываем сайт и чистим экран от баннеров)
    home_page.open(base_url)
    home_page.dismiss_welcome_banner()
    home_page.dismiss_cookie_banner()

    # 2. Навигация
    home_page.go_to_login_page()

    # 3. Действие (Action)
    login_page.fill_login_form("fake_user@example.com", "wrong_password123")

    # 4. Проверка (Assert)
    expected_error = "Invalid email or password."
    actual_error = login_page.get_error_message_text()

    assert expected_error in actual_error, f"Expected error '{expected_error}', but got '{actual_error}'"