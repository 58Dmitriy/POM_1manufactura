from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType
from utils.test_data import *


class OrderMakePage(BasePage):
    """Страница оформления заказа"""

    TITLE = (By.XPATH, "//h2[contains(text(),'Тип покупателя и регион доставки')]")  # текст "Товары для всадников"
    INDIVIDUAL_RADIOBUTTON = (By.XPATH, "//input[@name='PERSON_TYPE' and @value='1']") # радиокнопка "Физ.лицо"
    PAYMENT_UPON_DELIVERY_RADIOBUTTON = (By.XPATH, "//input[@id='ID_PAY_SYSTEM_ID_13']") # радиокнопка "Оплата при получении"

    # Раздел "Покупатель"
    LASTNAME = (By.XPATH, "//input[@id='soa-property-65']") # поле для ввода "Фамилия"
    NAME = (By.XPATH, "//input[@id='soa-property-64']") # поле для ввода "Имя"
    SURNAME = (By.XPATH, "//input[@id='soa-property-66']") # поле для ввода "Отчество"
    TELEPHONE = (By.XPATH, "//input[@id='soa-property-4']") # поле для ввода "Телефон"
    EMAIL = (By.XPATH, "//input[@id='soa-property-5']") # поле для ввода "Email"

    # Раздел "О персональных данных"
    CHECKBOX_PERSONAL_DATA = (By.XPATH, "//div[@class='bx-soa-orderSave-consent']//input[@type='checkbox']")
    # чекбокс "О персональных данных"
    ACCEPT = (By.XPATH, "//span[text()='Принимаю']") # кнопка "Принимаю"

    PLACE_ORDER_BUTTON = (By.XPATH, "//a[@href='javascript:void(0)' and contains(text(),'Оформить заказ')]")
    # кнопка "Оформить заказ"


    @allure.step("Проверяем наличие текста на странице")
    def title(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.TITLE)
            )
            result = element.text
            allure.attach(result, name="Текст заголовка", attachment_type=AttachmentType.TEXT)
            return result
        except TimeoutException:
            allure.attach(f"❌ Не появился за {timeout}сек", name="Текст заголовка", attachment_type=AttachmentType.TEXT)
            raise Exception(f"Заголовок не появился за {timeout} секунд")

    @allure.step("Проверить, что открыта страница 'Тип покупателя и регион доставки'")
    def verify_order_make_page_opened(self):
        actual_title = self.title().lower()
        expected_title = "тип покупателя и регион доставки"
        assert actual_title == expected_title, \
            f"Заголовок страницы '{actual_title}' не соответствует ожидаемому '{expected_title}'"

    @allure.step("Нажимаем радиокнопку 'Физ.лицо'")
    def individual_radiobutton(self):
        radiobutton = self.driver.find_element(*self.INDIVIDUAL_RADIOBUTTON)
        self.driver.execute_script("arguments[0].click();", radiobutton)
        allure.attach("✅", name="Радиокнопка выбрана", attachment_type=AttachmentType.TEXT)

    @allure.step("Нажимаем радиокнопку 'Оплата при получении'")
    def payment_upon_delivery_radiobutton(self):
        radiobutton = self.driver.find_element(*self.PAYMENT_UPON_DELIVERY_RADIOBUTTON)
        self.driver.execute_script("arguments[0].click();", radiobutton)
        allure.attach("✅", name="Способ оплаты выбран", attachment_type=AttachmentType.TEXT)

    @allure.step("Заполняем данные о покупателе")
    def enter_information_about_the_buyer(self, buyer_info):
        self.driver.execute_script(f"document.getElementById('soa-property-65').value = '{buyer_info.last_name}'")
        allure.attach(buyer_info.last_name, name="Фамилия", attachment_type=AttachmentType.TEXT)
        self.driver.execute_script(f"document.getElementById('soa-property-64').value = '{buyer_info.name}'")
        allure.attach(buyer_info.name, name="Имя", attachment_type=AttachmentType.TEXT)
        self.driver.execute_script(f"document.getElementById('soa-property-66').value = '{buyer_info.surname_name}'")
        allure.attach(buyer_info.surname_name, name="Отчество", attachment_type=AttachmentType.TEXT)
        self.driver.execute_script(f"document.getElementById('soa-property-4').value = '{buyer_info.phone}'")
        allure.attach(buyer_info.phone, name="Телефон", attachment_type=AttachmentType.TEXT)
        self.driver.execute_script(f"document.getElementById('soa-property-5').value = '{buyer_info.email}'")
        allure.attach(buyer_info.email, name="Email", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверяем наличие товара")
    def product_check(self, product_name):
        product_locator = (By.XPATH, f"//div[@class='bx-soa-item-title']/child::a[contains(text(),'{product_name}')]")
        result = self.get_text(product_locator)
        allure.attach(result, name="Название товара", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Принимаем согласие на обработку персональных данных")
    def consent_to_the_processing_of_personal_data(self):
        checkbox = self.driver.find_element(*self.CHECKBOX_PERSONAL_DATA)
        self.driver.execute_script("arguments[0].click();", checkbox)
        allure.attach("✅", name="Чекбокс отмечен", attachment_type=AttachmentType.TEXT)

        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ACCEPT)
        )
        self.driver.execute_script("arguments[0].click();", accept_button)
        allure.attach("✅", name="Согласие принято", attachment_type=AttachmentType.TEXT)

    @allure.step("Нажимаем кнопку 'Оформить заказ'")
    def place_order(self):
        button = self.driver.find_element(*self.PLACE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
        allure.attach("✅", name="Заказ оформлен", attachment_type=AttachmentType.TEXT)