import pytest
from pages.home_page import HomePage


@pytest.mark.ui
def test_welcome_banner_dismiss(page, base_url):
    """
    Тест-кейс: Проверка закрытия приветственного баннера на главной странице.
    Шаги:
    1. Открыть главную страницу Juice Shop.
    2. Нажать кнопку 'Dismiss' на баннере.
    3. Убедиться, что логотип сайта отображается (страница доступна).
    """
    # 1. Инициализируем Page Object
    home_page = HomePage(page)

    # 2. Переходим на главную страницу
    home_page.open(base_url)

    # 3. Закрываем раздражающий баннер
    home_page.dismiss_welcome_banner()

    # 4. Проверяем (Assert), что логотип теперь виден
    assert home_page.is_logo_visible() is True, "Логотип сайта не найден после закрытия баннера!"