from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object для главной страницы Juice Shop."""

    # === Локаторы ===
    WELCOME_BANNER_DISMISS_BTN = "[aria-label='Close Welcome Banner']"
    COOKIE_CONSENT_BTN = "[aria-label='dismiss cookie message']"

    # Кнопки навигации в верхнем меню
    ACCOUNT_BTN = "button#navbarAccount"
    LOGIN_MENU_ITEM = "button#navbarLoginButton"

    # === Методы ===
    def dismiss_welcome_banner(self):
        """Закрывает приветственный баннер, если он появился."""
        self.click_element(self.WELCOME_BANNER_DISMISS_BTN)

    def dismiss_cookie_banner(self):
        """Закрывает баннер о согласии на использование куки."""
        self.click_element(self.COOKIE_CONSENT_BTN)

    def go_to_login_page(self):
        """Кликает по меню Account -> Login для перехода на страницу авторизации."""
        self.click_element(self.ACCOUNT_BTN)
        self.click_element(self.LOGIN_MENU_ITEM)