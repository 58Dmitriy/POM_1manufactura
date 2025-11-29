import pytest
from pages.header import HeaderPage
from pages.vsadnikam_page import VsadnikamPage
from pages.horses_page import HorsesPage
from pages.favorites_page import FavoritesPage
from fixtures.parametrize_fixtures import *
from pages.product_card_page import ProductCardPage
import allure
from allure_commons.types import AttachmentType

@pytest.mark.ui
@pytest.mark.smoke
def test_add_in_favorites_from_catalog(driver):
    header_page = HeaderPage(driver)
    horses_page = VsadnikamPage(driver)
    favorites_page = FavoritesPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.add_multiple_to_favorites(FAVORITES_PRODUCTS)
    header_page.go_to_favorites_page()

    # Проверяем ВСЕ товары из FAVORITES_PRODUCTS
    for bx_id in FAVORITES_PRODUCTS:
        with allure.step(f"Проверяем наличие товара {bx_id} в избранном"):
            assert favorites_page.is_product_in_favorites_by_bx_id(bx_id)
            allure.attach("✅", name="Товар присутствует", attachment_type=AttachmentType.TEXT)

    # Удаляем ВСЕ товары из FAVORITES_PRODUCTS
    for bx_id in FAVORITES_PRODUCTS:
        with allure.step(f"Удаляем товар {bx_id} из избранного"):
            favorites_page.remove_from_favorites(bx_id)
            allure.attach("🗑️", name="Товар удален", attachment_type=AttachmentType.TEXT)

    allure.attach(f"✅ Обработано товаров: {len(FAVORITES_PRODUCTS)}",
                  name="Итог операции", attachment_type=AttachmentType.TEXT)


@halter_product_parametrize
@pytest.mark.ui
@pytest.mark.smoke
def test_add_in_favorites(driver, bx_id, product_name):
    header_page = HeaderPage(driver)
    horses_page = VsadnikamPage(driver)
    favorites_page = FavoritesPage(driver)
    product_card_page = ProductCardPage(driver)

    header_page.open_home_page()
    header_page.go_to_horses_page()
    horses_page.open_product_card_with_pagination(bx_id)
    assert product_card_page.is_text_present(product_name)
    product_card_page.add_in_favorites()
    header_page.go_to_favorites_page()
    assert not favorites_page.is_empty_favorites_displayed()
    assert favorites_page.is_product_in_favorites_by_bx_id(bx_id)
