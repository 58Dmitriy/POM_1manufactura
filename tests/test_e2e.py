import allure

from pages.header import HeaderPage
from pages.authorization import Authorization
from  pages.profile_page import Profile
from pages.cart_page import CartPage
from pages.stable_page import StablePage
from pages.order_make_page import OrderMakePage
from pages.order_page import OrderPage
from fixtures.parametrize_fixtures import *
from utils.auth_helper import *
from utils.test_data import *


@pytest.mark.ui
@pytest.mark.smoke
# @pytest.mark.skip
@allure.title("Полное оформление заказа")
def test_placing_an_order(driver):
    authorization_page = Authorization(driver)
    login, password = get_auth_credentials()
    profile_page = Profile(driver)
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    stable_page = StablePage(driver)
    order_make_page = OrderMakePage(driver)
    order_page = OrderPage(driver)

    authorization_page.open_login_page()
    authorization_page.login(login, password)
    profile_page.verify_profile_page_opened()

    header_page.open_home_page()
    header_page.go_to_stable_page()
    stable_page.verify_stable_page_opened()

    bx_id, product_name = stable_page.get_random_product()
    stable_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    cart_page.is_product_in_cart_by_name(product_name)
    cart_page.go_to_purchase()
    order_make_page.verify_order_make_page_opened()

    order_make_page.individual_radiobutton()
    order_make_page.payment_upon_delivery_radiobutton()
    order_make_page.enter_information_about_the_buyer(TEST_BUYER)
    order_make_page.product_check(product_name)
    order_make_page.consent_to_the_processing_of_personal_data()
    order_make_page.place_order()
    order_page.verify_payment_page_opened()

