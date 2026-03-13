from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object для главной страницы Juice Shop."""

    # === ЛОКАТОРЫ ===
    # Баннеры и логотип
    WELCOME_BANNER_DISMISS_BTN = "[aria-label='Close Welcome Banner']"
    COOKIE_CONSENT_BTN = "[aria-label='dismiss cookie message']"
    LOGO = "button[aria-label='Back to homepage']"

    # Навигация
    ACCOUNT_BTN = "button#navbarAccount"
    LOGIN_MENU_ITEM = "button#navbarLoginButton"

    # Поиск и товары (Используем надежные селекторы без динамических цифр!)
    SEARCH_ICON = "#searchQuery"
    SEARCH_INPUT = "mat-search-bar input"  # Ищем input внутри блока поиска
    PRODUCT_TITLE = "div.item-name"
    PRODUCT_DIALOG = "mat-dialog-container"
    DIALOG_TITLE = "mat-dialog-container h1"

    # === МЕТОДЫ ===
    def dismiss_welcome_banner(self):
        self.click_element(self.WELCOME_BANNER_DISMISS_BTN)

    def dismiss_cookie_banner(self):
        self.click_element(self.COOKIE_CONSENT_BTN)

    def is_logo_visible(self) -> bool:
        return self.page.locator(self.LOGO).is_visible()

    def go_to_login_page(self):
        self.click_element(self.ACCOUNT_BTN)
        self.click_element(self.LOGIN_MENU_ITEM)

    def search_for_product(self, query: str):
        # 1. Кликаем на саму лупу (весь блок поиска)
        self.click_element("#searchQuery")

        # 2. Обязательно ждем полсекунды, пока отработает анимация
        self.page.wait_for_timeout(500)

        # 3. БРОНЕБОЙНЫЙ ЛОКАТОР: Ищем input СТРОГО внутри блока #searchQuery
        search_input = self.page.locator("#searchQuery input")

        # 4. МАГИЯ: force=True пробивает любые прозрачные слои Angular!
        search_input.click(force=True)
        search_input.fill(query)
        search_input.press("Enter")

        # 5. Ждем загрузки карточек товаров
        self.page.locator(self.PRODUCT_TITLE).first.wait_for(state="visible")

    def get_first_product_name(self) -> str:
        return self.page.locator(self.PRODUCT_TITLE).first.inner_text()

    def click_first_product(self):
        self.page.locator(self.PRODUCT_TITLE).first.click()
        self.page.locator(self.PRODUCT_DIALOG).wait_for(state="visible")

    def get_product_dialog_title(self) -> str:
        return self.page.locator(self.DIALOG_TITLE).inner_text()