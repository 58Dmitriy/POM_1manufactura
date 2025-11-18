from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.bace_page import BasePage
import allure


class FavoritesPage(BasePage):
    """Страница избранных товаров"""

    TITLE = (By.XPATH, "//h1[contains(text(),'Список избранных товаров пуст.')]")  # текст "Товары для всадников"


    def is_product_in_favorites_by_bx_id(self, bx_id):
        """Проверяет наличие товара в избранном по bx_id"""
        try:
            element = self.driver.find_element(By.ID, bx_id)
            return element.is_displayed()
        except:
            return False

    def is_empty_favorites_displayed(self):
        """Проверяет отображается ли сообщение о пустом списке избранного"""
        print("=== ПРОВЕРКА ПУСТОГО ИЗБРАННОГО ===")

        try:
            element = self.driver.find_element(*self.TITLE)
            print(f"✅ Элемент заголовка найден")
            print(f"Текст элемента: '{element.text}'")
            print(f"Элемент отображается: {element.is_displayed()}")
            print(f"Содержит нужный текст: {'Список избранных товаров пуст' in element.text}")

            result = element.is_displayed() and "Список избранных товаров пуст" in element.text
            print(f"Результат проверки: {result}")
            return result

        except Exception as e:
            print(f"❌ Элемент не найден: {e}")
            return False

    def wait_for_empty_favorites_message(self, timeout=10):
        """Ожидает появление сообщения о пустом избранном"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITLE))
            return True
        except:
            return False

    def has_favorites_items(self):
        """Проверяет есть ли товары в избранном"""
        try:
            items = self.driver.find_elements(By.CLASS_NAME, "favorites-list__item")
            return len(items) > 0
        except:
            return False

    def remove_from_favorites(self, bx_id):
        """Удаление товара из избранного"""
        element = self.driver.find_element(By.XPATH, f"//div[@id='{bx_id}']")
        checkbox = element.find_element(By.XPATH, ".//input[@type='checkbox']")
        self.driver.execute_script("arguments[0].click();", checkbox)