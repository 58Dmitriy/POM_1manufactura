from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType


class VsadnikamPage(BasePage):
    """Страница раздела каталога товаров "Всадникам" """

    TITLE = (By.XPATH, "//h1[text()='Товары для всадников']")  # текст "Товары для всадников"

    @allure.step("Проверяем наличие текста на странице")
    def title(self):
        result = self.get_text(self.TITLE)
        allure.attach(result, name="📋 Заголовок", attachment_type=AttachmentType.TEXT)
        return result







