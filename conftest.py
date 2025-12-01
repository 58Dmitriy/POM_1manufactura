import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure


# Подключаем параметризации
pytest_plugins = ["fixtures.parametrize_fixtures"]

@pytest.fixture
def driver():
    """Фикстура для запуска и завершения браузера"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    with allure.step("Запуск Chrome браузера"):
        driver = webdriver.Chrome(options=options)
        allure.attach(
            f"Браузер: Chrome\nВерсия: {driver.capabilities['browserVersion']}\nHeadless: True",
            name="Browser Info",
            attachment_type=allure.attachment_type.TEXT
        )
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()
