import pytest
from pages.authorization import Authorization
from pages.profile_page import Profile
from utils.auth_helper import *
from utils.test_data import *


@pytest.mark.ui
@pytest.mark.smoke
def test_success_change_data(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    assert profile_page.title().lower() == "мои данные"

    profile_page.enter_tell_about_yourself(ABOUT_YOURSELF)
    profile_page.select_gender("woman")
    profile_page.save_information()
    assert profile_page.save_info().lower() == "изменения сохранены"

@pytest.mark.ui
@pytest.mark.smoke
def test_success_change_password(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    assert profile_page.title().lower() == "мои данные"

    profile_page.change_password(CHANGE_PASSWORD)
    profile_page.save_information()
    assert profile_page.save_info().lower() == "изменения сохранены"

@pytest.mark.ui
@pytest.mark.regression
def test_incorrect_password_confirmation(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    assert profile_page.title().lower() == "мои данные"

    profile_page.change_password(INCORRECT_PASSWORD_CONFIRMATION)
    profile_page.save_information()
    assert profile_page.error_text().lower() == "неверное подтверждение пароля."

@pytest.mark.ui
@pytest.mark.regression
def test_missing_current_password(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    assert profile_page.title().lower() == "мои данные"

    profile_page.change_password(MISSING_CURRENT_PASSWORD)
    profile_page.save_information()
    assert profile_page.error_text().lower() == "неверный текущий пароль."