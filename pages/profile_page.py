from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data import *

class Profile(BasePage):
    """Страница профиля"""

    TITLE = (By.XPATH, '//h1[text()="Мои данные"]') # текст "Мои данные"
    SAVE_INFO = (By.XPATH, "//font[@class='notetext']") # текст "Изменения сохранены"
    ERROR_TEXT = (By.XPATH, "//font[@class='errortext']") # текст "Неверное подтверждение пароля."
    SAVE_BUTTON = (By.XPATH, "//input[@name='save']") # кнопка "Сохранить изменения"
    ADDRESS_BOOK_BUTTON = (By.XPATH, "//a[contains(@class,'cabinet-nav__link--address')]") # кнопка "Адресная книга"

    # Блок "Расскажи о себе"
    LAST_NAME = (By.XPATH, "//input[@name='LAST_NAME']") # поле ввода "Фамилия"
    NAME = (By.XPATH, "//input[@name='NAME']") # поле ввода "Имя"
    SECOND_NAME = (By.XPATH, "//input[@name='SECOND_NAME']")  # поле ввода "Отчёство"
    ## Дата рождения
    # DAY = (By.XPATH, "//input[@id='day-label']")
    # MONTH = (By.XPATH, "//option[@value='03']")
    # YEAR = (By.XPATH, "//input[@id='year-label']")

    PERSONAL_PHONE = (By.XPATH, "//input[@name='PERSONAL_PHONE']") # поле ввода "Телефон"
    EMAIL = (By.XPATH, "//input[@name='EMAIL']")  # поле ввода "EMAIL"
    ## Радиокнопки пола (gender)
    GENDER_MAN = (By.XPATH, "//label[@for='form-gender-man']") # радиокнопка "gender-man"
    GENDER_WOMAN = (By.XPATH, "//label[@for='form-gender-woman']") # радиокнопка "gender-woman"

    # Блок "Ваш пароль"
    CURRENT_PASSWORD = (By.XPATH, "//input[@placeholder='Текущий пароль']") # поле ввода "Текущий пароль"
    NEW_PASSWORD = (By.XPATH, "//input[@name='NEW_PASSWORD']") # поле ввода "Новый пароль"
    NEW_PASSWORD_CONFIRM = (By.XPATH, "//input[@name='NEW_PASSWORD_CONFIRM']") # поле ввода "Повторите новый пароль"


    @allure.step("Проверить наличие заголовка на странице")
    def title(self):
        return self.get_text(self.TITLE)

    @allure.step("Указать изменённые данные в личном кабинете")
    def enter_tell_about_yourself(self, info: dict):
        self.type(self.LAST_NAME, info["last_name"])
        self.type(self.NAME, info["name"])
        self.type(self.SECOND_NAME, info["second_name"])
        self.type(self.PERSONAL_PHONE, info["phone"])
        self.type(self.EMAIL, info["email"])

    @allure.step("Выбираем пол")
    def select_gender(self, gender: str):
        gender = gender.lower().strip()

        if gender in ['man']:
            self.click(self.GENDER_MAN)
        elif gender in ['woman']:
            self.click(self.GENDER_WOMAN)
        else:
            raise ValueError(f"Неизвестный пол: '{gender}'. Используй 'man' или 'woman'")

    @allure.step("Нажать кнопку 'Сохранить изменения'")
    def save_information(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    @allure.step("Проверяем сообщение об успешном сохранении изменений ")
    def save_info(self):
        return self.get_text(self.SAVE_INFO)

    @allure.step("Указываем текущий, новый пароль и подтверждаем новый пароль")
    def change_password(self, password: Password):
        self.type(self.CURRENT_PASSWORD, password.current_password)
        self.type(self.NEW_PASSWORD, password.new_password)
        self.type(self.NEW_PASSWORD_CONFIRM, password.new_password_confirm)

    @allure.step("Проверяем сообщение об ошибке")
    def error_text(self):
        return self.get_text(self.ERROR_TEXT)

    @allure.step("Нажать кнопку 'Адресная книга'")
    def go_to_address_book(self):
        self.driver.find_element(*self.ADDRESS_BOOK_BUTTON).click()