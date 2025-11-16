import pytest
from pages.header import HeaderPage
from pages.vsadnikam_page import VsadnikamPage
from pages.horses_page import HorsesPage
from pages.cart_page import CartPage
from fixtures.parametrize_fixtures import *
import time


@breeches_product_parametrize
@pytest.mark.ui
@pytest.mark.smoke
def test_successful_addition_of_product_to_cart(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    vsadnikam_page = VsadnikamPage(driver)

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    vsadnikam_page.add_product_to_cart_by_id(bx_id)
    header_page.go_to_cart_page()
    assert cart_page.TITLE_CONTENTS_IN_THE_BASKET
    assert cart_page.is_product_in_cart_by_name(product_name)


@polo_product_parametrize
@pytest.mark.ui
@pytest.mark.smoke
def test_product_search_and_add_via_pagination(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    vsadnikam_page = VsadnikamPage(driver)

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    vsadnikam_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    assert cart_page.TITLE_CONTENTS_IN_THE_BASKET
    assert cart_page.is_product_in_cart_by_name(product_name)


@halter_product_parametrize
@pytest.mark.ui
@pytest.mark.smoke
def test_product_quantity_can_be_increased_and_decreased(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    horses_page = HeaderPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    assert cart_page.TITLE_CONTENTS_IN_THE_BASKET
    assert cart_page.is_product_in_cart_by_name(product_name)

    cart_page.plus_value()
    cart_page.plus_value()
    cart_page.minus_value()
    assert cart_page.counter_value() == 2


@halter_product_parametrize
@pytest.mark.ui
@pytest.mark.smoke
def test_manual_entry_of_products(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    horses_page = HeaderPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    assert cart_page.TITLE_CONTENTS_IN_THE_BASKET
    assert cart_page.is_product_in_cart_by_name(product_name)

    cart_page.enter_quantity_of_goods(3)
    assert cart_page.counter_value() == 3

@halter_product_parametrize
def test_open_product_card(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    horses_page = HeaderPage(driver)

    header_page.open_home_page()
    horses_page.open_product_card_with_pagination(bx_id)
    time.sleep(10)

