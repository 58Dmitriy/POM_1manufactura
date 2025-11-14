from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure


class HorsesPage(BasePage):
    """Страница раздела каталога товаров "Лошадям" """

    TITLE = (By.XPATH, "//h1[text()='Товары для лошадей']")  # текст "Товары для всадников"