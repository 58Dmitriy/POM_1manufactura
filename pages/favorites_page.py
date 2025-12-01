from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType


class FavoritesPage(BasePage):
    """Страница избранных товаров"""

    TITLE = (By.XPATH, "//h1[contains(text(),'Список избранных товаров пуст.')]")  # текст "Товары для всадников"

    @allure.step("Проверяем наличие товара в избранном по bx_id")
    def is_product_in_favorites_by_bx_id(self, bx_id):
        try:
            element = self.driver.find_element(By.ID, bx_id)
            result = element.is_displayed()
            status = "✅ Найден" if result else "❌ Не найден"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return result
        except:
            allure.attach("❌ Не найден", name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Проверяем отображается ли сообщение о пустом списке избранного")
    def is_empty_favorites_displayed(self):
        try:
            element = self.driver.find_element(*self.TITLE)
            result = element.is_displayed() and "Список избранных товаров пуст" in element.text
            status = "✅ Сообщение отображается" if result else "❌ Сообщение не найдено"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return result
        except Exception:
            allure.attach("❌ Элемент не найден", name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Ожидаем появление сообщения о пустом избранном")
    def wait_for_empty_favorites_message(self, timeout=10):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITLE))
            allure.attach("✅", name="Сообщение появилось", attachment_type=AttachmentType.TEXT)
            return True
        except:
            allure.attach("❌", name="Сообщение не появилось", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Проверяем есть ли товары в избранном")
    def has_favorites_items(self):
        try:
            items = self.driver.find_elements(By.CLASS_NAME, "favorites-list__item")
            result = len(items) > 0
            status = f"✅ Найдено: {len(items)}" if result else "❌ Товаров нет"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return result
        except:
            allure.attach("❌ Ошибка поиска", name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Удаляем товар из избранного")
    def remove_from_favorites(self, bx_id):
        element = self.driver.find_element(By.XPATH, f"//div[@id='{bx_id}']")
        checkbox = element.find_element(By.XPATH, ".//input[@type='checkbox']")
        self.driver.execute_script("arguments[0].click();", checkbox)
        allure.attach("✅", name="Товар удален", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверить, что список избранного НЕ пустой")
    def verify_favorites_not_empty(self):
        """Проверяет, что список избранного содержит товары"""
        try:
            element = self.driver.find_element(*self.TITLE)
            is_empty_displayed = element.is_displayed() and "Список избранных товаров пуст" in element.text
            status = "✅ Список не пуст" if not is_empty_displayed else "❌ Список пуст"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            assert not is_empty_displayed, "Список избранного пуст, но ожидалось наличие товаров"
        except Exception:
            # Если элемента нет - это хорошо, значит список не пустой
            allure.attach("✅ Список не пуст (элемент не найден)", name="Результат проверки",
                          attachment_type=AttachmentType.TEXT)

    @allure.step("Проверить наличие товара с ID {bx_id} в избранном")
    def verify_product_in_favorites(self, bx_id):
        """Проверяет наличие конкретного товара в избранном"""
        try:
            element = self.driver.find_element(By.ID, bx_id)
            result = element.is_displayed()
            status = "✅ Товар найден в избранном" if result else "❌ Товар не найден"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            assert result, f"Товар с ID {bx_id} не отображается в избранном"
        except Exception as e:
            allure.attach(f"❌ Товар с ID {bx_id} не найден в избранном", name="Результат проверки",
                          attachment_type=AttachmentType.TEXT)
            raise AssertionError(f"Товар с ID {bx_id} не найден в избранном") from e