import pytest
from pages.header import HeaderPage
from pages.vsadnikam_page import VsadnikamPage
from pages.cart_page import CartPage

@pytest.mark.parametrize(
    "bx_id",
    [
        "bx_3966226736_24865"
    ]
)
@pytest.mark.ui
@pytest.mark.smoke
def test_successful_addition_of_product_to_cart(driver, bx_id):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    vsadnikam_page = VsadnikamPage(driver)

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    vsadnikam_page.add_product_to_cart_by_id(bx_id)
    header_page.go_to_cart_page()
    assert cart_page.TITLE_CONTENTS_IN_THE_BASKET
    assert cart_page.is_product_in_cart_by_name("Бриджи подростковые с силиконовой леей белый")


@pytest.mark.parametrize(
    "info",
    [
        pytest.param(("bx_3966226736_24218", "Ветровка детская Lucky Gina синий"),
                     id = f'bx_3966226736_24218, Ветровка детская Lucky Gina синий')
    ]
)
@pytest.mark.ui
@pytest.mark.smoke
def test_product_search_and_add_via_pagination(driver, info):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    vsadnikam_page = VsadnikamPage(driver)
    bx_id, product_name = info

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    vsadnikam_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    assert cart_page.TITLE_CONTENTS_IN_THE_BASKET
    assert cart_page.is_product_in_cart_by_name(product_name)
