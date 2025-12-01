from pages.header import HeaderPage
from pages.vsadnikam_page import VsadnikamPage
from pages.favorites_page import FavoritesPage
from fixtures.parametrize_fixtures import *
from pages.product_card_page import ProductCardPage
import allure


@allure.feature("Favorites")
@pytest.mark.no_authorization
@pytest.mark.ui
@pytest.mark.smoke
@allure.title("Добавление конкретного товара в 'Избранное'")
def test_add_in_favorites(driver):
    header_page = HeaderPage(driver)
    horses_page = VsadnikamPage(driver)
    favorites_page = FavoritesPage(driver)
    product_card_page = ProductCardPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    bx_id, product_name = horses_page.get_random_product()
    horses_page.open_product_card_with_pagination(bx_id)
    product_card_page.verify_text_present(product_name)
    product_card_page.add_in_favorites()
    header_page.go_to_favorites_page()
    favorites_page.verify_favorites_not_empty()
    favorites_page.verify_product_in_favorites(bx_id)
