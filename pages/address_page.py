from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.step("Проверить наличие заголовка на странице")
    def title(self):
        return self.get_text(self.TITLE)

    @allure.step("Нажать кнопку 'Добавить' адрес")
    def add_new_address(self):
        self.driver.find_element(*self.ADD_ADDRESS_BUTTON).click()

    @allure.step("Вводим адрес для доставки")
    def enter_address(self, address: AddressData):
        self.type(self.COUNTRY, address.country)
        self.type(self.CITY, address.city)
        self.type(self.STREET, address.street)
        self.type(self.BUILDING, address.building)
        self.type(self.AP, address.ap)

    @allure.step("Нажать кнопку 'Сохранить изменения'")
    def save_information(self):
        self.driver.find_element(*self.SAVE_ADDRESS_BUTTON).click()