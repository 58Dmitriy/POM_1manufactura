import pytest


halter_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",  # названия параметров в тесте
    [
        ("bx_3966226736_25050", "Недоуздок на неопреновых подложках MIU Equestrian Neo 2.0 фиолетовый")
    ],
    ids=["Недоуздок фиолетовый"]  # ID для отчета
)

polo_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",
    [
        ("bx_3966226736_24728", "Поло рубашка мужская с длинным рукавом чёрный")
    ],
    ids=["Поло рубашка чёрная"]
)

breeches_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",
    [
        ("bx_3966226736_24865", "Бриджи подростковые с силиконовой леей белый")
    ],
    ids=["Бриджи белые"]
)

breeches_2_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",
    [
        ("bx_3966226736_24713", "Брегинсы ANGEL бежевый")
    ],
    ids=["Брегинсы бежевые"]
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


STABLE_PRODUCTS = [
    ("bx_3966226736_22291", "Тазик резиновый 12л"),
    ("bx_3966226736_15149", "Набор для уборки HO")
]

stable_product_parametrize = pytest.mark.parametrize(
    "bx_id, product_name",
    [
        ("bx_3966226736_23560", "Игрушка для лошади большой шар для корма фиолетовый")
    ],
    ids=["Шар для корма фиолетовый"]
)