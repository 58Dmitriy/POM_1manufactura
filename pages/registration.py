from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
import time


class Registration(BasePage):
    """Страница регистрации"""

    NAME = (By.XPATH, "//input[@name='USER_NAME']")
    LAST_NAME = (By.XPATH, "//input[@name='USER_LAST_NAME']")
    USER_LOGIN = (By.XPATH, "//input[@name='USER_LOGIN']")
    USER_PASSWORD = (By.XPATH, "//input[@name='USER_PASSWORD']")
    USER_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='USER_CONFIRM_PASSWORD']")
    USER_EMAIL = (By.XPATH, "//input[@name='USER_EMAIL']")
    CAPTCHA_WORD = (By.XPATH, "//input[@name='captcha_word']")
    USER_AGREEMENT = (By.XPATH, "//input[@name='USER_AGREEMENT']")
    ACCEPT_BUTTON = (By.XPATH, "//span[text()='Принимаю']")
    REGISTRATION_BUTTON = (By.XPATH, "//input[@name='Register']")

    @allure.step("Открыть страницу регистрации")
    def open_registration_page(self):
        self.open("https://1manufactura.ru/profile/?register=yes")

    @allure.step("Ввести name, last_name, user_login, user_password, "
                 "user_confirm_password, user_email, captcha_word "
                 "и нажать кнопку 'Регистрация'")
    def new_registration(self,
                         name,
                         last_name,
                         user_login,
                         user_password,
                         user_confirm_password,
                         user_email,
                         captcha_word
                         ):
        self.type(self.NAME, name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.USER_LOGIN, user_login)
        self.type(self.USER_PASSWORD, user_password)
        self.type(self.USER_CONFIRM_PASSWORD, user_confirm_password)
        self.type(self.USER_EMAIL, user_email)
        self.type(self.CAPTCHA_WORD, captcha_word)
        self.click(self.USER_AGREEMENT)
        self.click(self.ACCEPT_BUTTON)
        time.sleep(30)
        self.click(self.REGISTRATION_BUTTON)