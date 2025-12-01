import pytest
from pages.registration_page import Registration
from  pages.profile_page import Profile
import allure


@allure.feature("Registration")
@pytest.mark.ui
@pytest.mark.skip
@allure.title("Успешная регистрация нового пользователя")
def test_successful_registration(driver):
    registration_page = Registration(driver)
    profile_page = Profile(driver)

    registration_page.open_registration_page()
    registration_page.new_registration("",
                                       "",
                                       "test18",
                                       "0000000",
                                       "0000000",
                                       "test18@mail.ru",
                                       "")
    profile_page.verify_profile_page_opened()