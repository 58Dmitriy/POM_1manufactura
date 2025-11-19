from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure


class OrderPage(BasePage):
    """Страница подтверждения о совершении заказа"""

    TITLE = (By.XPATH, "//div[@class='bx-soa-page-payment-name' and contains(text(),"
                       "'Оплата при получении (картой или наличными при получении заказа)')]")  # текст для проверки


    @allure.step("Проверяем наличие текста на странице")
    def title(self, timeout=10):
        """Ожидает и возвращает текст заголовка"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.TITLE)
            )
            return element.text
        except TimeoutException:
            raise Exception(f"Заголовок не появился за {timeout} секунд")