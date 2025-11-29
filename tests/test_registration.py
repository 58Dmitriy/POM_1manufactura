import pytest
from pages.registration_page import Registration
from  pages.profile_page import Profile


@pytest.mark.ui
# @pytest.mark.skip
def test_successful_login(driver):
    registration_page = Registration(driver)
    profile_page = Profile(driver)

    registration_page.open_registration_page()
    registration_page.new_registration("",
                                       "",
                                       "test15",
                                       "0000000",
                                       "0000000",
                                       "test15@mail.ru",
                                       "")
    assert profile_page.title().lower() == "мои данные"