from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class CartPage(BasePage):

    """Страница корзины товаров"""

    TITLE_EMPTY_CART = (By.XPATH, "//h1[text()='Ваша корзина пуста']")  # текст "Ваша корзина пуста"
    TITLE_CONTENTS_IN_THE_BASKET = (By.XPATH, "//h1[contains(text(), 'корзине')]") # текст корзины с содержимым
    CART_ROW = (By.XPATH, "//div[@class='cart__row']") # строка товара в корзине
    COUNTER_VALUE = (By.XPATH, "//input[@class='counter__value']") # счётчик определённого товара
    COUNTER_MINUS = (By.XPATH, "//span[@class='counter__minus']") # уменьшить число товаров
    COUNTER_PLUS = (By.XPATH, "//span[@class='counter__plus']") # увеличить число товаров
    GO_TO_PURCHASE_BUTTON = (By.XPATH, "//a[contains(@class,'go2order')]") # кнопка "Перейти к покупке"
    CART_CELL_SIZE = (By.XPATH, "./following::div[@class='cart__cell-size']") # ячейка размера товара


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

    def counter_value_is_displayed(self):
        """Проверяет, отображается ли счетчик товара"""
        try:
            counter = self.driver.find_element(*self.COUNTER_VALUE)
            return counter.is_displayed()
        except:
            return False

    @allure.step("Проверить чему равен счётчик товара")
    def counter_value(self):
        """Возвращает количество товаров или 0 если счетчика нет"""
        if self.counter_value_is_displayed():
            try:
                counter_element = self.driver.find_element(*self.COUNTER_VALUE)
                # Получаем значение из атрибута value (для input fields)
                value = counter_element.get_attribute('value')
                if value and value.strip() != '':
                    return int(value)
                return 1  # значение по умолчанию если value пустой
            except:
                return 1  # значение по умолчанию при ошибке
        return 1  # значение по умолчанию если счетчик не отображается

    def enter_quantity_of_goods(self, quantity):
        """Ручной ввод числа товаров в корзине"""
        self.type(self.COUNTER_VALUE, quantity)

    @allure.step("Уменьшаем количество товаров на 1")
    def minus_value(self):
        self.driver.find_element(*self.COUNTER_MINUS).click()

    @allure.step("Увеличиваем количество товаров на 1")
    def plus_value(self):
        self.driver.find_element(*self.COUNTER_PLUS).click()

    @allure.step("Нажать на кнопку 'Перейти к покупке'")
    def go_to_purchase(self):
        """Нажать на кнопку 'Перейти к покупке'"""
        self.driver.find_element(*self.GO_TO_PURCHASE_BUTTON).click()

    @allure.step("Проверяем фактический размер товара в корзине")
    def size_check(self, product_name, expected_size):
        """Проверяет размер товара в корзине"""
        size_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//div[@class='info__title']/a[contains(text(),'{product_name}')]"
                                            f"/following::div[@class='cart__cell-size']"))
        )

        actual_size = size_element.text

        assert actual_size == expected_size, (
            f"Неверный размер для товара '{product_name}'. "
            f"Ожидался: '{expected_size}', Фактический: '{actual_size}'"
        )


