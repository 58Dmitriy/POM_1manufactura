from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType


class StablePage(BasePage):
    """Страница раздела каталога товаров "Конюшня" """

    TITLE = (By.XPATH, "//h1[text()='Товары для конюшни']")  # текст "Товары для конюшни"

    @allure.step("Проверяем наличие текста на странице")
    def title(self):
        result = self.get_text(self.TITLE)
        allure.attach(result, name="📄 Текст страницы", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Проверить, что открыта страница 'Товары для конюшни'")
    def verify_stable_page_opened(self):
        actual_title = self.title().lower()
        expected_title = "товары для конюшни"
        assert actual_title == expected_title, \
            f"Заголовок страницы '{actual_title}' не соответствует ожидаемому '{expected_title}'"