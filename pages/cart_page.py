from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure


class CartPage(BasePage):

    """Страница корзины товаров"""

    TITLE_EMPTY_CART = (By.XPATH, "//h1[text()='Ваша корзина пуста']")  # текст "Ваша корзина пуста"
    TITLE_CONTENTS_IN_THE_BASKET = (By.XPATH, "//h1[contains(text(), 'корзине')]") # текст корзины с содержимым
    CART_ROW = (By.XPATH, "//div[@class='cart__row']") # строка товара в корзине

    @allure.step("Открыть страницу корзины товаров")
    def open_cart_page(self):
        self.open("https://1manufactura.ru/personal/cart/")

    @allure.step("Проверяем что товар с указанным названием в корзине")
    def is_product_in_cart_by_name(self, expected_product_name):
        """Проверить, что товар с указанным названием есть в корзине"""
        cart_items = self.driver.find_elements(*self.CART_ROW)
        for item in cart_items:
            product_name_element = item.find_element(By.CLASS_NAME, "info__title")
            if expected_product_name in product_name_element.text:
                return True
        return False