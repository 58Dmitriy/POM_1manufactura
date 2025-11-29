from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType

class Authorization(BasePage):
    """Страница авторизации"""

    USER_LOGIN = (By.XPATH, '//*[@name="USER_LOGIN"]') # поле "Логин"
    USER_PASSWORD = (By.XPATH, '//*[@name="USER_PASSWORD"]') # поле "Пароль"
    LOGIN_BUTTON = (By.XPATH, '//*[@name="Login"]') # кнопка "Войти"
    ERROR_MESSAGE = (By.XPATH, '//*[@class="errortext"]') # сообщение об ошибке

    @allure.step("Открываем страницу логина")
    def open_login_page(self):
        self.open("https://1manufactura.ru/profile/")
        allure.attach("✅", name="Страница открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Авторизация пользователя")
    def login(self, userlogin, password):
        self.type(self.USER_LOGIN, userlogin)
        allure.attach(userlogin, name="Логин", attachment_type=AttachmentType.TEXT)
        self.type(self.USER_PASSWORD, password)
        allure.attach("***", name="Пароль", attachment_type=AttachmentType.TEXT)
        self.click(self.LOGIN_BUTTON)
        allure.attach("✅", name="Вход", attachment_type=AttachmentType.TEXT)

    @allure.step("Сообщение об ошибке авторизации")
    def error_message(self):
        result = self.get_text(self.ERROR_MESSAGE)
        allure.attach(result, name="Ошибка", attachment_type=AttachmentType.TEXT)
        return result