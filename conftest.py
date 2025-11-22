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
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
