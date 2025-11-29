from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType
import time


class Registration(BasePage):
    """Страница регистрации"""

    NAME = (By.XPATH, "//input[@name='USER_NAME']") # поле "Имя"
    LAST_NAME = (By.XPATH, "//input[@name='USER_LAST_NAME']") # поле "Фамилия"
    USER_LOGIN = (By.XPATH, "//input[@name='USER_LOGIN']") # поле "Логин"
    USER_PASSWORD = (By.XPATH, "//input[@name='USER_PASSWORD']") # поле "Пароль"
    USER_CONFIRM_PASSWORD = (By.XPATH, "//input[@name='USER_CONFIRM_PASSWORD']") # поле "Подтверждение пароля"
    USER_EMAIL = (By.XPATH, "//input[@name='USER_EMAIL']") # поле "E-Mail"
    CAPTCHA_WORD = (By.XPATH, "//input[@name='captcha_word']") # поле "Защитное поле на картинке"
    USER_AGREEMENT = (By.XPATH, "//input[@name='USER_AGREEMENT']") # чекбокс "О персональных данных"
    ACCEPT_BUTTON = (By.XPATH, "//span[text()='Принимаю']") # кнопка "Принять"
    REGISTRATION_BUTTON = (By.XPATH, "//input[@name='Register']") # кнопка "Регистрация"

    @allure.step("Открываем страницу регистрации")
    def open_registration_page(self):
        self.open("https://1manufactura.ru/profile/?register=yes")
        allure.attach("📝", name="Страница регистрации открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Регистрация нового пользователя")
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
        allure.attach(name, name="Имя", attachment_type=AttachmentType.TEXT)
        self.type(self.LAST_NAME, last_name)
        allure.attach(last_name, name="Фамилия", attachment_type=AttachmentType.TEXT)
        self.type(self.USER_LOGIN, user_login)
        allure.attach(user_login, name="Логин", attachment_type=AttachmentType.TEXT)
        self.type(self.USER_PASSWORD, user_password)
        allure.attach("***", name="Пароль", attachment_type=AttachmentType.TEXT)
        self.type(self.USER_CONFIRM_PASSWORD, user_confirm_password)
        allure.attach("***", name="Подтверждение пароля", attachment_type=AttachmentType.TEXT)
        self.type(self.USER_EMAIL, user_email)
        allure.attach(user_email, name="Email", attachment_type=AttachmentType.TEXT)
        self.type(self.CAPTCHA_WORD, captcha_word)
        allure.attach(captcha_word, name="Капча", attachment_type=AttachmentType.TEXT)
        self.click(self.USER_AGREEMENT)
        self.click(self.ACCEPT_BUTTON)
        allure.attach("подтверждаем", name="Пользовательское соглашение", attachment_type=AttachmentType.TEXT)
        with allure.step("Ожидание ручного ввода капчи (30 секунд)"):
            allure.attach("Ожидание ручного ввода текста с картинки", name="Пояснение",
                          attachment_type=AttachmentType.TEXT)
            time.sleep(30) # необходимо время для ручного ввода текста с картинки для проверки
        self.click(self.REGISTRATION_BUTTON)
        allure.attach("✓", name="Форма отправлена", attachment_type=AttachmentType.TEXT)