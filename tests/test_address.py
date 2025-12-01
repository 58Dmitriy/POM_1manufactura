import pytest
from pages.authorization import Authorization
from pages.profile_page import Profile
from pages.address_page import Address
from utils.auth_helper import *
from utils.test_data import *
import allure

@allure.feature("Address")
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Корректное указание адреса")
def test_correct_address(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    address_page = Address(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

    profile_page.go_to_address_book()
    address_page.verify_address_book_opened()

    address_page.add_new_address()
    address_page.enter_address(CORRECT_ADDRESS)
    address_page.save_information()

