import pytest


halter_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",  # названия параметров в тесте
    [
        ("bx_3966226736_25050", "Недоуздок на неопреновых подложках MIU Equestrian Neo 2.0 фиолетовый")
    ],
    ids=["halter_purple"]  # ID для отчета
)

polo_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",
    [
        ("bx_3966226736_24728", "Поло рубашка мужская с длинным рукавом чёрный")
    ],
    ids=["polo_black"]
)

breeches_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",
    [
        ("bx_3966226736_24865", "Бриджи подростковые с силиконовой леей белый")
    ],
    ids=["breeches_white"]
)


FAVORITES_PRODUCTS = [
    "bx_3966226736_25050",
    "bx_3966226736_24966",
    "bx_3966226736_24815"
]

horse_favorites_product_parametrize = pytest.mark.parametrize(
    "bx_id",
    FAVORITES_PRODUCTS
)