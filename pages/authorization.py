from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure

class Authorization(BasePage):
    """Страница авторизации"""

    USER_LOGIN = (By.XPATH, '//*[@name="USER_LOGIN"]')
    USER_PASSWORD = (By.XPATH, '//*[@name="USER_PASSWORD"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@name="Login"]')
    ERROR_MESSAGE = (By.XPATH, '//*[@class="errortext"]')

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open("https://1manufactura.ru/profile/")

    @allure.step("Ввести userlogin, password и нажать кнопку 'Войти'")
    def login(self, userlogin, password):
        self.type(self.USER_LOGIN, userlogin)
        self.type(self.USER_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Сообщение об ошибке авторизации")
    def error_message(self):
        return self.get_text(self.ERROR_MESSAGE)