import pytest
from pages.authorization import Authorization
from pages.profile_page import Profile
from utils.auth_helper import *
from utils.test_data import *
import allure


@allure.feature("User data")
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Успешное изменение данных пользователя")
def test_success_change_data(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

    profile_page.enter_tell_about_yourself(ABOUT_YOURSELF)
    profile_page.select_gender("woman")
    profile_page.save_information()
    profile_page.verify_changes_saved()

@allure.feature("Changing the user password")
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Успешное изменение пароля")
def test_success_change_password(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

    profile_page.change_password(CHANGE_PASSWORD)
    profile_page.save_information()
    profile_page.verify_changes_saved()

@allure.feature("Changing the user password")
@pytest.mark.ui
@pytest.mark.regression
@allure.title("Неверное подтверждение пароля")
def test_incorrect_password_confirmation(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

    profile_page.change_password(INCORRECT_PASSWORD_CONFIRMATION)
    profile_page.save_information()
    profile_page.verify_password_confirmation_error()

@allure.feature("Changing the user password")
@pytest.mark.ui
@pytest.mark.regression
@allure.title("Неверный ввод текущего пароля")
def test_missing_current_password(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

    profile_page.change_password(MISSING_CURRENT_PASSWORD)
    profile_page.save_information()
    profile_page.verify_current_password_error()