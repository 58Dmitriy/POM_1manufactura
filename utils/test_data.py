from dataclasses import dataclass

@dataclass
class BuyerInfo:
    name: str
    last_name: str
    surname_name: str
    phone: str
    email: str

@dataclass
class Password:
    current_password: str
    new_password: str
    new_password_confirm: str


# Тестовые данные для покупателя в e2e тесте: test_placing_an_order
TEST_BUYER = BuyerInfo(
    name="test",
    last_name="test",
    surname_name="test",
    phone="+79999999999",
    email="test10@mail.ru"
)

# Тестовые данные для пароля в test_profile тесте: test_success_change_data
ABOUT_YOURSELF = {
    "last_name": "Иванов",
    "name": "Иван",
    "second_name": "Иванович",
    "day": "19",
    "month": "11", # месяц указывать в формате от 01 до 12
    "year": "1970",
    "phone": "+71234567788",
    "email": "test20@mail.ru",
}

# Тестовые данные для пароля в test_profile тесте: test_success_change_password
CHANGE_PASSWORD = Password(
    current_password = "0000000",
    new_password = "1111111",
    new_password_confirm = "1111111"
)

# Тестовые данные для пароля в test_profile тесте: test_incorrect_password_confirmation
INCORRECT_PASSWORD_CONFIRMATION =Password(
current_password = "0000000",
    new_password = "1111111",
    new_password_confirm = "123456789"
)

# Тестовые данные для пароля в test_profile тесте: test_missing_current_password
MISSING_CURRENT_PASSWORD = Password(
    current_password="",
    new_password="0000000",
    new_password_confirm="0000000"
)
