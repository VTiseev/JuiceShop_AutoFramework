from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех Page Objects. Содержит общие методы Playwright."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Открывает указанный URL."""
        self.page.goto(url)

    def click_element(self, selector: str):
        """Ожидает появления элемента в DOM дерева и кликает по нему."""
        self.page.locator(selector).wait_for(state="visible")
        self.page.locator(selector).click()