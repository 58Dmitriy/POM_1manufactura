from dataclasses import dataclass

@dataclass
class BuyerInfo:
    name: str
    last_name: str
    surname_name: str
    phone: str
    email: str

# Тестовые данные для покупателя в e2e тесте: test_placing_an_order
TEST_BUYER = BuyerInfo(
    name="test",
    last_name="test",
    surname_name="test",
    phone="+79999999999",
    email="test10@mail.ru"
)

