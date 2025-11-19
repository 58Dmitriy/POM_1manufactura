import pytest
from pages.authorization import Authorization
from  pages.profile_page import Profile
from utils.auth_helper import *


@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    assert profile_page.title().lower() == "мои данные"

@pytest.mark.parametrize(
    "creds",
    [
        pytest.param(("Super", "test123"), id = f'Super, test123'),
        pytest.param(("SuperTest", "test12"), id = f'SuperTest, test12')
    ]
)

@pytest.mark.ui
@pytest.mark.smoke
def test_login_invalid_login(driver, creds):
    authorization_page = Authorization(driver)
    authorization_page.open_login_page()
    user_login, password = creds
    authorization_page.login(user_login, password)
    assert authorization_page.error_message() == "Неверный логин или пароль."

