import pytest

import pages
from pages.authorization import Authorization
from pages.profile_page import Profile
from pages.address_page import Address
from utils.auth_helper import *
from utils.test_data import *


@pytest.mark.ui
@pytest.mark.smoke
def test_correct_address(driver):
    authorization_page = Authorization(driver)
    profile_page = Profile(driver)
    address_page = Address(driver)
    login, password = get_auth_credentials()

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    assert profile_page.title().lower() == "мои данные"

    profile_page.go_to_address_book()
    assert address_page.title().lower() == "адресная книга"

    address_page.add_new_address()
    address_page.enter_address(CORRECT_ADDRESS)
    address_page.save_information()

