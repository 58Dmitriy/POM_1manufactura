from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure


class HorsesPage(BasePage):
    """Страница раздела каталога товаров "Лошадям" """

    TITLE = (By.XPATH, "//h1[text()='Товары для лошадей']")  # текст "Товары для всадников"