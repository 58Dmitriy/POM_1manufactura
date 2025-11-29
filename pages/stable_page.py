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