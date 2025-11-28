from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from pages.bace_page import BasePage
import allure
import time


class ProductCardPage(BasePage):
    """Страница карточки товара"""

    TITLE = (By.XPATH, "//h1[@class='title-page']") # для проверки названия товара
    FAVORITES_BUTTON = (By.XPATH, "//a[@class='links__chosen']") # кнопка добавления в избранное
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@data-href='/personal/cart/']") # кнопка добавления в корзину
    SIZE_SELECT = (By.XPATH, "//span[@class='current']") # раскрыть селектор размеров
    SIZE_LIST = (By.XPATH, "//ul[@class='list']") # список с размерами

    @allure.step("Проверить название товара")
    def is_text_present(self, text):
        """Проверяет наличие текста на странице"""
        return text in self.driver.page_source

    @allure.step("Добавить товар в 'Избранное'")
    def add_in_favorites(self):
        """Нажать кнопку 'Добавить в избранное'"""
        self.driver.find_element(*self.FAVORITES_BUTTON).click()

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        """Добавляет товар в корзину"""
        buttons = self.driver.find_elements(
            By.XPATH,"//button[contains(text(), 'Корзину') or contains(text(), 'Добавить')]"
        )
        for btn in buttons:
            if btn.is_displayed() and 'добав' in btn.text.lower():
                btn.click()
                break

    @allure.step("Выбрать размер товара")
    def select_size(self, size):
        """Выбирает размер товара"""
        self.driver.find_element(*self.SIZE_SELECT).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//li[@data-value='{size}']"))
        )

        size_element = self.driver.find_element(By.XPATH, f"//li[@data-value='{size}']")
        size_element.click()

        return True
