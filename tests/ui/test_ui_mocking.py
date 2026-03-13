import pytest
from pages.home_page import HomePage


@pytest.mark.ui
def test_mock_product_search(page, base_url):
    """
    Тест-кейс: Проверка UI с помощью подмены ответа от сервера (Network Mocking).
    Шаги:
    1. Перехватить API-запрос поиска товаров.
    2. Подсунуть фейковый ответ (Stub) с придуманным товаром.
    3. Выполнить поиск через UI.
    4. Убедиться, что фронтенд успешно отрисовал наш фейковый товар.
    """
    # 1. Подготавливаем наш СТАБ (фейковый ответ, который "якобы" прислал бэкенд)
    mock_response = {
        "status": "success",
        "data": [
            {
                "id": 999,
                "name": "Senior QA Magic Juice",
                "description": "Автоматически находит все баги на сайте.",
                "price": 9999.99,
                "image": "apple_juice.jpg"
            }
        ]
    }

    # 2. МАГИЯ PLAYWRIGHT: Перехватываем сеть (Network Interception)
    # Звездочки ** означают: перехвати любой запрос, где есть "/rest/products/search"
    page.route("**/rest/products/search**", lambda route: route.fulfill(
        status=200,
        json=mock_response
    ))

    # 3. Обычные шаги UI теста
    home_page = HomePage(page)
    home_page.open(base_url)
    home_page.dismiss_welcome_banner()
    home_page.dismiss_cookie_banner()

    # Вводим "Apple" в поиск. Фронтенд отправит запрос на бэкенд,
    # но Playwright перехватит его и мгновенно отдаст наш mock_response!
    home_page.search_for_product("Apple")

    # 4. Проверяем, что на витрине появился НАШ товар
    first_product_name = home_page.get_first_product_name()

    assert first_product_name == "Senior QA Magic Juice", \
        f"Mock failed! Expected 'Senior QA Magic Juice', but got '{first_product_name}'"