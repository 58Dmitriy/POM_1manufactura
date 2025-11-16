from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure


class FavoritesPage(BasePage):
    """Страница избранных товаров"""

    TITLE = (By.XPATH, "//h1[contains(text(),'Список избранных товаров пуст.')]")  # текст "Товары для всадников"
    FAVORITES_ITEM = (By.XPATH, "//div[@id='{bx_id}']") # товар в избранном

    def is_product_in_favorites_by_bx_id(self, bx_id):
        """Проверяет наличие товара в избранном по bx_id"""
        try:
            element = self.driver.find_element(By.ID, bx_id)
            return element.is_displayed()
        except:
            return False


    def is_empty_favorites_displayed(self):
        """Проверяет отображается ли сообщение о пустом списке избранного"""
        try:
            element = self.driver.find_element(*self.TITLE)
            return "Список избранных товаров пуст" in element.text
        except:
            return False


    def has_favorites_items(self):
        """Проверяет есть ли товары в избранном"""
        try:
            items = self.driver.find_elements(By.CLASS_NAME, "favorites-list__item")
            return len(items) > 0
        except:
            return False