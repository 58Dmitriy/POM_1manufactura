from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure


class VsadnikamPage(BasePage):
    """Страница раздела каталога товаров "Всадникам" """

    TITLE = (By.XPATH, "//h1[text()='Товары для всадников']")  # текст "Товары для всадников"









