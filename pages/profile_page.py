from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from utils.test_data import *
from allure_commons.types import AttachmentType

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
    ## Дата рождения (не реализовано/отложено)
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


    @allure.step("Проверяем наличие заголовка на странице")
    def title(self):
        result = self.get_text(self.TITLE)
        allure.attach(result, name="Заголовок", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Проверить, что открыта страница 'Мои данные'")
    def verify_profile_page_opened(self):
        actual_title = self.title().lower()
        expected_title = "мои данные"
        assert actual_title == expected_title\
            , f"Заголовок страницы '{actual_title}' не соответствует ожидаемому '{expected_title}'"


    @allure.step("Вводим изменяемые данные в личном кабинете")
    def enter_tell_about_yourself(self, info: dict):
        self.type(self.LAST_NAME, info["last_name"])
        allure.attach(info["last_name"], name="👤 Фамилия", attachment_type=AttachmentType.TEXT)
        self.type(self.NAME, info["name"])
        allure.attach(info["name"], name="👤 Имя", attachment_type=AttachmentType.TEXT)
        self.type(self.SECOND_NAME, info["second_name"])
        allure.attach(info["second_name"], name="👤 Отчество", attachment_type=AttachmentType.TEXT)
        self.type(self.PERSONAL_PHONE, info["phone"])
        allure.attach(info["phone"], name="📞 Телефон", attachment_type=AttachmentType.TEXT)
        self.type(self.EMAIL, info["email"])
        allure.attach(info["email"], name="📧 Email", attachment_type=AttachmentType.TEXT)

    @allure.step("Выбираем пол")
    def select_gender(self, gender: str):
        gender = gender.lower().strip()

        if gender in ['man']:
            self.click(self.GENDER_MAN)
            allure.attach("👨", name="Пол выбран", attachment_type=AttachmentType.TEXT)
        elif gender in ['woman']:
            self.click(self.GENDER_WOMAN)
            allure.attach("👩", name="Пол выбран", attachment_type=AttachmentType.TEXT)
        else:
            allure.attach("❌", name="Ошибка выбора", attachment_type=AttachmentType.TEXT)
            raise ValueError(f"Неизвестный пол: '{gender}'. Используй 'man' или 'woman'")

    @allure.step("Нажимаем кнопку 'Сохранить изменения'")
    def save_information(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()
        allure.attach("💾", name="Изменения сохранены", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверяем сообщение об успешном сохранении изменений ")
    def save_info(self):
        result = self.get_text(self.SAVE_INFO)
        allure.attach(result, name="✅ Сообщение", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Проверить, что изменения успешно сохранены")
    def verify_changes_saved(self):
        actual_message = self.save_info().lower()
        expected_message = "изменения сохранены"
        assert actual_message == expected_message, \
            f"Сообщение '{actual_message}' не соответствует ожидаемому '{expected_message}'"

    @allure.step("Изменение пароля пользователя")
    def change_password(self, password: Password):
        self.type(self.CURRENT_PASSWORD, password.current_password)
        allure.attach("введен", name="Текущий пароль", attachment_type=AttachmentType.TEXT)
        self.type(self.NEW_PASSWORD, password.new_password)
        allure.attach("введен", name="Новый пароль", attachment_type=AttachmentType.TEXT)
        self.type(self.NEW_PASSWORD_CONFIRM, password.new_password_confirm)
        allure.attach("введено", name="Подтверждение нового пароля", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверяем сообщение об ошибке")
    def error_text(self):
        result = self.get_text(self.ERROR_TEXT)
        allure.attach(result, name="❌ Ошибка", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Проверить сообщение об ошибке подтверждения пароля")
    def verify_password_confirmation_error(self):
        actual_error = self.error_text().lower()
        expected_error = "неверное подтверждение пароля."
        assert actual_error == expected_error, \
            f"Сообщение об ошибке '{actual_error}' не соответствует ожидаемому '{expected_error}'"

    @allure.step("Проверить сообщение об ошибке текущего пароля")
    def verify_current_password_error(self):
        actual_error = self.error_text().lower()
        expected_error = "неверный текущий пароль."
        assert actual_error == expected_error, \
            f"Сообщение об ошибке '{actual_error}' не соответствует ожидаемому '{expected_error}'"

    @allure.step("Нажимаем кнопку 'Адресная книга'")
    def go_to_address_book(self):
        self.driver.find_element(*self.ADDRESS_BOOK_BUTTON).click()
        allure.attach("📒", name="Адресная книга открыта", attachment_type=AttachmentType.TEXT)