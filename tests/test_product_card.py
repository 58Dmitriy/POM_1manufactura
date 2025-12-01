from pages.header import HeaderPage
from pages.vsadnikam_page import VsadnikamPage
from pages.horses_page import HorsesPage
from pages.product_card_page import ProductCardPage
from pages.cart_page import CartPage
from fixtures.parametrize_fixtures import *
import allure


@halter_product_parametrize
@allure.feature("Product size")
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Выбор размера товара")
def test_select_product_size(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    product_card_page = ProductCardPage(driver)
    horses_page = HorsesPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.open_product_card_with_pagination(bx_id)

    product_card_page.verify_text_present(product_name)
    product_card_page.select_size('full')
    product_card_page.add_to_cart()
    header_page.go_to_cart_page()
    cart_page.is_product_in_cart_by_name(product_name)
    cart_page.size_check(product_name, 'full')

@breeches_2_product_parametrize
@allure.feature("Product size")
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Выбор размера товара 2")
def test_2_select_product_size(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    product_card_page = ProductCardPage(driver)
    vsadnikam_page = VsadnikamPage(driver)

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    vsadnikam_page.open_product_card_with_pagination(bx_id)

    product_card_page.verify_text_present(product_name)
    product_card_page.select_size('S')
    product_card_page.add_to_cart()
    header_page.go_to_cart_page()
    cart_page.is_product_in_cart_by_name(product_name)
    cart_page.size_check(product_name, 'S')