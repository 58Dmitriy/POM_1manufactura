from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType


class OrderPage(BasePage):
    """Страница подтверждения о совершении заказа"""

    TITLE = (By.XPATH, "//div[@class='bx-soa-page-payment-name' and contains(text(),"
                       "'Оплата при получении (картой или наличными при получении заказа)')]")  # текст для проверки


    @allure.step("Проверяем наличие текста на странице")
    def title(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.TITLE)
            )
            result = element.text
            allure.attach(result,
                          name="Текст заголовка",
                          attachment_type=AttachmentType.TEXT
                          )
            return result
        except TimeoutException:
            allure.attach(f"❌ Не появился за {timeout}сек",
                          name="Текст заголовка",
                          attachment_type=AttachmentType.TEXT
                          )
            raise Exception(f"Заголовок не появился за {timeout} секунд")

    @allure.step("Проверить, что открыта страница 'Оплата при получении'")
    def verify_payment_page_opened(self):
        actual_title = self.title().lower()
        expected_title = "оплата при получении (картой или наличными при получении заказа)"
        assert actual_title == expected_title, \
            f"Заголовок страницы '{actual_title}' не соответствует ожидаемому '{expected_title}'"