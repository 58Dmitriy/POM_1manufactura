import pytest
from pages.authorization import Authorization
from pages.profile_page import Profile
from utils.auth_helper import *
import allure


@allure.feature("Authentication")
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Успешная авторизация")
def test_successful_login(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

@pytest.mark.parametrize(
    "creds",
    [
        pytest.param(("Super", "test123"), id = f'Super, test123'),
        pytest.param(("SuperTest", "test12"), id = f'SuperTest, test12')
    ]
)

@allure.feature("Authentication")
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Не успешная авторизация")
def test_login_invalid_login(driver, creds):
    authorization_page = Authorization(driver)
    authorization_page.open_login_page()
    user_login, password = creds
    authorization_page.login(user_login, password)
    authorization_page.verify_invalid_login_error()

@pytest.mark.parametrize(
    "creds",
    [
        pytest.param(("test19", "0000000"), id = f'test19, 0000000')
    ]
)

@allure.feature("Authentication")
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.login
@allure.title("Успешная авторизация")
def test_successful_login(driver, creds):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)

    authorization_page.open_login_page()
    user_login, password = creds
    authorization_page.login(user_login, password)
    profile_page.verify_profile_page_opened()

