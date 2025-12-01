from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType


class ProductCardPage(BasePage):
    """Страница карточки товара"""

    TITLE = (By.XPATH, "//h1[@class='title-page']") # для проверки названия товара
    FAVORITES_BUTTON = (By.XPATH, "//a[@class='links__chosen']") # кнопка добавления в избранное
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@data-href='/personal/cart/']") # кнопка добавления в корзину
    SIZE_SELECT = (By.XPATH, "//span[@class='current']") # раскрыть селектор размеров
    SIZE_LIST = (By.XPATH, "//ul[@class='list']") # список с размерами

    @allure.step("Проверяем название товара")
    def is_text_present(self, text):
        result = text in self.driver.page_source
        status = "✅ Найден" if result else "❌ Не найден"
        allure.attach(status, name="Результат поиска", attachment_type=AttachmentType.TEXT)
        return result

    @allure.step("Проверить, что название товара '{text}' отображается на странице")
    def verify_text_present(self, text):
        """Проверяет наличие текста на странице и вызывает assert"""
        result = text in self.driver.page_source
        status = "✅ Найден" if result else "❌ Не найден"
        allure.attach(status, name="Результат поиска", attachment_type=AttachmentType.TEXT)
        assert result, f"Текст '{text}' не найден на странице. Текущий URL: {self.driver.current_url}"

    @allure.step("Добавляем товар в 'Избранное'")
    def add_in_favorites(self):
        self.driver.find_element(*self.FAVORITES_BUTTON).click()
        allure.attach("✅", name="Товар добавлен", attachment_type=AttachmentType.TEXT)

    @allure.step("Добавляем товар в корзину")
    def add_to_cart(self):
        buttons = self.driver.find_elements(
            By.XPATH, "//button[contains(text(), 'Корзину') or contains(text(), 'Добавить')]"
        )
        for btn in buttons:
            if btn.is_displayed() and 'добав' in btn.text.lower():
                btn.click()
                allure.attach("✅", name="Товар добавлен", attachment_type=AttachmentType.TEXT)
                break
        else:
            allure.attach("❌", name="Кнопка не найдена", attachment_type=AttachmentType.TEXT)

    @allure.step("Выбираем размер товара")
    def select_size(self, size):
        self.driver.find_element(*self.SIZE_SELECT).click()
        allure.attach("✅", name="Список размеров открыт", attachment_type=AttachmentType.TEXT)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//li[@data-value='{size}']"))
        )

        size_element = self.driver.find_element(By.XPATH, f"//li[@data-value='{size}']")
        size_element.click()
        allure.attach("✅", name="Размер выбран", attachment_type=AttachmentType.TEXT)

        return True

