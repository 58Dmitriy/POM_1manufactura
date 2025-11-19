from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure

class Profile(BasePage):
    """Страница профиля"""

    TITLE = (By.XPATH, '//h1[text()="Мои данные"]') # текст "Мои данные"

    @allure.step("Проверяем наличие текста на странице")
    def title(self):
        return self.get_text(self.TITLE)