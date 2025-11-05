import pytest
from pages.authorization import Authorization
from  pages.profile import Profile


@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    authorization_page.open_login_page()
    authorization_page.login("SuperTest", "test123")
    assert profile_page.title().text.lower() == "мои данные"

@pytest.mark.ui
@pytest.mark.smoke
def test_login_invalid_login(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_login_page()
    authorization_page.login("Super", "test123")
    assert authorization_page.error_message().text == "Неверный логин или пароль."

@pytest.mark.ui
@pytest.mark.smoke
def test_login_invalid_password(driver):
    authorization_page = Authorization(driver)
    authorization_page.open_login_page()
    authorization_page.login("SuperTest", "test12")
    assert authorization_page.error_message().text == "Неверный логин или пароль."