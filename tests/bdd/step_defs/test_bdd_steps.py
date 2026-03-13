import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.login_page import LoginPage

# 1. Говорим Pytest-у, где лежат наши текстовые сценарии
scenarios('../features/ui_tests.feature')

# ==========================================
# 🛠️ Фикстуры для BDD
# ==========================================
@pytest.fixture
def home_page(page):
    """Инициализируем HomePage один раз для шагов"""
    return HomePage(page)

@pytest.fixture
def login_page(page):
    """Инициализируем LoginPage"""
    return LoginPage(page)

@pytest.fixture
def context():
    """Словарь-контекст. Нужен, чтобы передавать данные между шагами (When -> Then)"""
    return {}

# ==========================================
# 🟢 GIVEN (Дано / Предусловия)
# ==========================================
@given("I open the Juice Shop home page")
def open_home_page(home_page, base_url):
    home_page.open(base_url)

@given("I dismiss all welcome banners")
def dismiss_banners(home_page):
    home_page.dismiss_welcome_banner()
    home_page.dismiss_cookie_banner()

# ==========================================
# 🟡 WHEN (Когда / Действия)
# ==========================================
# parsers.parse позволяет вытаскивать переменные прямо из текста шага в кавычках!
@when(parsers.parse('I search for the product "{product_name}"'))
def search_product(home_page, product_name):
    home_page.search_for_product(product_name)

@when("I click on the first product on the board")
def click_first_product(home_page, context):
    # Сохраняем имя товара в контекст, чтобы потом сравнить его в THEN
    context["board_product_name"] = home_page.get_first_product_name()
    home_page.click_first_product()

@when("I navigate to the login page")
def navigate_to_login(home_page):
    home_page.go_to_login_page()

@when(parsers.parse('I try to login with email "{email}" and password "{password}"'))
def try_login(login_page, email, password):
    login_page.fill_login_form(email, password)

# ==========================================
# 🔵 THEN (Тогда / Проверки)
# ==========================================
@then(parsers.parse('the first result should contain "{product_name}"'))
def verify_search_result(home_page, product_name):
    actual_name = home_page.get_first_product_name()
    assert product_name in actual_name

@then("the product dialog title should match the product name")
def verify_dialog_title(home_page, context):
    dialog_title = home_page.get_product_dialog_title()
    assert context["board_product_name"] == dialog_title

@then(parsers.parse('I should see an error message "{error_msg}"'))
def verify_error_message(login_page, error_msg):
    actual_error = login_page.get_error_message_text()
    assert error_msg in actual_error

@then("the site logo should be visible")
def verify_logo_visible(home_page):
    assert home_page.is_logo_visible() is True