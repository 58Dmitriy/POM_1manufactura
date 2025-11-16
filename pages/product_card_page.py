from selenium.webdriver.common.by import By

from conftest import driver
from pages.bace_page import BasePage
import allure


class ProductCardPage(BasePage):
    """Страница карточки товара"""

    TITLE = (By.XPATH, "//h1[@class='title-page']")
    FAVORITES_BUTTON = (By.XPATH, "//a[@class='links__chosen']")

    def is_text_present(self, text):
        """Проверяет наличие текста на странице"""
        return text in self.driver.page_source

    def add_in_favorites(self):
        """Нажать кнопку 'Добавить в избранное'"""
        self.driver.find_element(*self.FAVORITES_BUTTON).click()