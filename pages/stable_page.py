from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure


class StablePage(BasePage):
    """Страница раздела каталога товаров "Конюшня" """

    TITLE = (By.XPATH, "//h1[text()='Товары для конюшни']")  # текст "Товары для конюшни"

    @allure.step("Проверяем наличие текста на странице")
    def title(self):
        """Проверяем наличие текста на странице"""
        return self.get_text(self.TITLE)