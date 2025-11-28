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

@dataclass
class AddressData:
    country: str
    city: str
    street: str
    building: str
    ap: str


# Тестовые данные для покупателя в e2e тесте: test_placing_an_order
TEST_BUYER = BuyerInfo(
    name="Иван",
    last_name="Иванов",
    surname_name="Иванович",
    phone="+79999999999",
    email="ivanivanov@mail.ru"
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
    "email": "test21@mail.ru",
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

# Тестовые данные для пароля в test_address тесте: test_correct_address
CORRECT_ADDRESS = AddressData(
    country="Россия",
    city="Москва",
    street="Карла Маркса",
    building="4",
    ap="1"
)
