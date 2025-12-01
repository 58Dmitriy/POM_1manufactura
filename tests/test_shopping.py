from pages.header import HeaderPage
from pages.vsadnikam_page import VsadnikamPage
from pages.cart_page import CartPage
from pages.stable_page import StablePage
from pages.product_card_page import ProductCardPage
from fixtures.parametrize_fixtures import *
import allure


@allure.feature("Adding product")
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Успешное добавление товара в корзину")
def test_successful_addition_of_product_to_cart(driver):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    vsadnikam_page = VsadnikamPage(driver)

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    bx_id, product_name = header_page.get_random_product()
    vsadnikam_page.add_product_to_cart_by_id(bx_id)
    header_page.go_to_cart_page()
    cart_page.verify_product_in_cart(product_name)

@allure.feature("Adding product with pagination")
@polo_product_parametrize
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Успешный поиск и добавление товара по страницам")
def test_product_search_and_add_via_pagination(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    vsadnikam_page = VsadnikamPage(driver)

    header_page.open_home_page()
    header_page.go_to_vsadnikam_page()
    vsadnikam_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    cart_page.verify_product_in_cart(product_name)

@allure.feature("Changing the quantity of goods")
@halter_product_parametrize
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Увеличение и уменьшение количества товаров в корзине")
def test_product_quantity_can_be_increased_and_decreased(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    horses_page = HeaderPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    cart_page.verify_cart_page_opened()
    cart_page.verify_product_in_cart(product_name)

    cart_page.plus_value()
    cart_page.plus_value()
    cart_page.minus_value()
    cart_page.verify_counter_value(2)

@allure.feature("Changing the quantity of goods")
@halter_product_parametrize
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Ручной ввод количества товара в корзине")
def test_manual_entry_of_products(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    cart_page = CartPage(driver)
    horses_page = HeaderPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.add_product_to_cart_by_id_with_pagination(bx_id)
    header_page.go_to_cart_page()
    cart_page.verify_product_in_cart(product_name)

    cart_page.enter_quantity_of_goods(3)
    cart_page.verify_counter_value(3)

@allure.feature("Open product card")
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Открытие карточки товара")
def test_open_product_card(driver):
    header_page = HeaderPage(driver)
    horses_page = HeaderPage(driver)
    product_card_page = ProductCardPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    bx_id, product_name = horses_page.get_random_product()
    horses_page.open_product_card_with_pagination(bx_id)
    product_card_page.verify_text_present(product_name)


