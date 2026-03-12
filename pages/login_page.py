from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object для страницы авторизации."""

    # === Локаторы ===
    EMAIL_INPUT = "input#email"
    PASSWORD_INPUT = "input#password"
    LOGIN_BTN = "button#loginButton"
    ERROR_MESSAGE = "div.error" # Блок с текстом ошибки

    # === Методы ===
    def fill_login_form(self, email: str, password: str):
        """Заполняет форму авторизации и нажимает Login."""
        # fill() - это метод Playwright, который стирает старый текст и вводит новый
        self.page.locator(self.EMAIL_INPUT).fill(email)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.click_element(self.LOGIN_BTN)

    def get_error_message_text(self) -> str:
        """Получает текст сообщения об ошибке."""
        self.page.locator(self.ERROR_MESSAGE).wait_for(state="visible")
        return self.page.locator(self.ERROR_MESSAGE).inner_text()