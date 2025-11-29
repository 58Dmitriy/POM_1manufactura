from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


    @allure.step("Открываем страницу корзины товаров")
    def open_cart_page(self):
        self.open("https://1manufactura.ru/personal/cart/")
        allure.attach("✅", name="Корзина открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверяем что товар с указанным названием в корзине")
    def is_product_in_cart_by_name(self, expected_product_name):
        cart_items = self.driver.find_elements(*self.CART_ROW)
        for item in cart_items:
            product_name_element = item.find_element(By.CLASS_NAME, "info__title")
            if expected_product_name in product_name_element.text:
                allure.attach("✅", name="Товар найден", attachment_type=AttachmentType.TEXT)
                return True

        allure.attach("❌", name="Товар не найден", attachment_type=AttachmentType.TEXT)
        return False

    @allure.step("Проверяем отображается ли счетчик товара")
    def counter_value_is_displayed(self):
        try:
            counter = self.driver.find_element(*self.COUNTER_VALUE)
            result = counter.is_displayed()
            status = "✅ Отображается" if result else "❌ Не отображается"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return result
        except:
            allure.attach("❌ Элемент не найден", name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Проверяем чему равен счётчик товара")
    def counter_value(self):
        if self.counter_value_is_displayed():
            try:
                counter_element = self.driver.find_element(*self.COUNTER_VALUE)
                # Получаем значение из атрибута value (для input fields)
                value = counter_element.get_attribute('value')
                if value and value.strip() != '':
                    result = int(value)
                    allure.attach(str(result), name="Значение счетчика", attachment_type=AttachmentType.TEXT)
                    return result
                allure.attach("1", name="Значение счетчика (по умолчанию)", attachment_type=AttachmentType.TEXT)
                return 1  # значение по умолчанию если value пустой
            except:
                allure.attach("1", name="Значение счетчика (ошибка)", attachment_type=AttachmentType.TEXT)
                return 1  # значение по умолчанию при ошибке

        allure.attach("1", name="Значение счетчика (не отображается)", attachment_type=AttachmentType.TEXT)
        return 1  # значение по умолчанию если счетчик не отображается

    @allure.step("Указываем количество товаров: {quantity}")
    def enter_quantity_of_goods(self, quantity):
        self.type(self.COUNTER_VALUE, quantity)
        allure.attach("✅", name="Количество обновлено", attachment_type=AttachmentType.TEXT)

    @allure.step("Уменьшаем количество товаров на 1")
    def minus_value(self):
        self.driver.find_element(*self.COUNTER_MINUS).click()
        allure.attach("✅", name="Количество уменьшено", attachment_type=AttachmentType.TEXT)

    @allure.step("Увеличиваем количество товаров на 1")
    def plus_value(self):
        self.driver.find_element(*self.COUNTER_PLUS).click()
        allure.attach("✅", name="Количество увеличено", attachment_type=AttachmentType.TEXT)

    @allure.step("Нажимаем на кнопку 'Перейти к покупке'")
    def go_to_purchase(self):
        self.driver.find_element(*self.GO_TO_PURCHASE_BUTTON).click()
        allure.attach("✅", name="Переход к покупке", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверяем фактический размер товара в корзине")
    def size_check(self, product_name, expected_size):
        size_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//div[@class='info__title']/a[contains(text(),'{product_name}')]"
                                            f"/following::div[@class='cart__cell-size']"))
        )

        actual_size = size_element.text

        allure.attach(f"Ожидаемый: {expected_size}\nФактический: {actual_size}",
                      name="Размеры товара", attachment_type=AttachmentType.TEXT)

        assert actual_size == expected_size, (
            f"Неверный размер для товара '{product_name}'. "
            f"Ожидался: '{expected_size}', Фактический: '{actual_size}'"
        )

        allure.attach("✅", name="Размер совпадает", attachment_type=AttachmentType.TEXT)