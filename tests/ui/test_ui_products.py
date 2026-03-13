import pytest
from pages.home_page import HomePage


@pytest.mark.ui
def test_search_product(page, base_url):
    """
    Тест-кейс: Поиск существующего товара.
    Шаги:
    1. Открыть главную страницу, закрыть баннеры.
    2. Ввести 'Apple' в строку поиска и нажать Enter.
    3. Убедиться, что в названии первого найденного товара есть слово 'Apple'.
    """
    home_page = HomePage(page)

    # 1. Предусловия
    home_page.open(base_url)
    home_page.dismiss_welcome_banner()
    home_page.dismiss_cookie_banner()

    # 2. Действие: ищем яблоко
    search_query = "Apple"
    home_page.search_for_product(search_query)

    # 3. Проверка: берем текст первого товара и проверяем, что там есть "Apple"
    first_product_name = home_page.get_first_product_name()
    assert search_query in first_product_name, f"Expected '{search_query}' to be in '{first_product_name}'"


@pytest.mark.ui
def test_open_product_details(page, base_url):
    """
    Тест-кейс: Открытие всплывающего окна с описанием товара.
    Шаги:
    1. Открыть главную страницу, закрыть баннеры.
    2. Запомнить название первого товара на витрине.
    3. Кликнуть по этому товару.
    4. Убедиться, что открылось окно и заголовок совпадает с названием товара.
    """
    home_page = HomePage(page)

    # 1. Предусловия
    home_page.open(base_url)
    home_page.dismiss_welcome_banner()
    home_page.dismiss_cookie_banner()

    # 2. Действие: запоминаем имя на витрине и кликаем
    product_name_on_board = home_page.get_first_product_name()
    home_page.click_first_product()

    # 3. Проверка: имя во всплывающем окне должно совпадать с именем на витрине
    dialog_title = home_page.get_product_dialog_title()
    assert product_name_on_board == dialog_title, f"Expected dialog title to be '{product_name_on_board}', got '{dialog_title}'"