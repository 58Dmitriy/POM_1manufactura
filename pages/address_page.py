from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType
from utils.test_data import *

class Address(BasePage):
    """Страница адресной книги внутри личного кабинета"""

    TITLE = (By.XPATH, '//h1[text()="Адресная книга"]')  # текст "Адресная книга"
    ADD_ADDRESS_BUTTON = (By.XPATH, "//button[contains(@class,'mainForm__btn-add')]") # кнопка "Добавить" адрес
    SAVE_ADDRESS_BUTTON = (By.XPATH, "//button[contains(@class,'address-save')]") # кнопка "Сохранить изменения"
    COUNTRY = (By.XPATH, "//input[@name='country']") # поле ввода "Страна"
    CITY = (By.XPATH, "//input[@name='city']") # поле ввода "Город"
    STREET = (By.XPATH, "//input[@name='street']") # поле ввода "Улица"
    BUILDING = (By.XPATH, "//input[@name='building']") # поле ввода "Дом"
    AP = (By.XPATH, "//input[@name='ap']") # поле ввода "Номер квартиры"

    @allure.step("Проверяем наличие заголовка на странице")
    def title(self):
        result = self.get_text(self.TITLE)
        allure.attach(result, name="Заголовок", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Нажимаем кнопку 'Добавить' адрес")
    def add_new_address(self):
        self.driver.find_element(*self.ADD_ADDRESS_BUTTON).click()
        allure.attach("✓", name="Добавлено", attachment_type=AttachmentType.TEXT)

    @allure.step("Вводим адрес для доставки")
    def enter_address(self, address: AddressData):
        self.type(self.COUNTRY, address.country)
        allure.attach(address.country, name="🌍 Страна", attachment_type=AttachmentType.TEXT)
        self.type(self.CITY, address.city)
        allure.attach(address.city, name="🏙️ Город", attachment_type=AttachmentType.TEXT)
        self.type(self.STREET, address.street)
        allure.attach(address.street, name="🛣️ Улица", attachment_type=AttachmentType.TEXT)
        self.type(self.BUILDING, address.building)
        allure.attach(address.building, name="🏢 Дом", attachment_type=AttachmentType.TEXT)
        self.type(self.AP, address.ap)
        allure.attach(address.ap, name="🚪 Квартира", attachment_type=AttachmentType.TEXT)

    @allure.step("Нажимаем кнопку 'Сохранить изменения'")
    def save_information(self):
        self.driver.find_element(*self.SAVE_ADDRESS_BUTTON).click()
        allure.attach("✓", name="Сохранено", attachment_type=AttachmentType.TEXT)