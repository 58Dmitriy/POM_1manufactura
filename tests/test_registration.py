import pytest
from pages.registration import Registration
from  pages.profile import Profile
import time


@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(driver):
    registration_page = Registration(driver)
    profile_page = Profile(driver)
    registration_page.open_registration_page()
    registration_page.new_registration("",
                                       "",
                                       "test10",
                                       "0000000",
                                       "0000000",
                                       "test10@mail.ru",
                                       "")
    assert profile_page.title().text.lower() == "мои данные"