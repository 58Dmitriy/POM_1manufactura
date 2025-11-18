from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class BasePage(object):
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста '{text}'")
    def type(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text


    BACK_BUTTON = (By.XPATH, "//a[@class='back']") # кнопка "назад"
    NEXT_PAGE_BUTTON = (By.XPATH, "//a[@class='pagination__arrow pagination__arrow--next']") # кнопка перехода на следующую страницу

    CATALOG_ITEM = "//div[@class='catalog']/child::div[@id='{bx_id}']" # товар в каталоге
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(@class, 'js-add-to-basket')]")  # кнопка "Добавить в корзину"
    FAVORITES_BUTTON = (By.XPATH, ".//input[@type='checkbox']") # кнопка добавления в избранное

    @allure.step("Ищем товар по bx_id")
    def find_product_by_id(self, bx_id):
        """Найти продукт по 'bx_id' """
        try:
            locator = (By.XPATH, self.CATALOG_ITEM.format(bx_id=bx_id))
            elements = self.driver.find_elements(*locator)
            return elements[0] if elements else None
        except:
            return None

    @allure.step("Находим и добавляем товар в корзину по bx_id")
    def add_product_to_cart_by_id(self, bx_id):
        """Добавить товар в корзину по 'bx_id' """
        element = self.find_product_by_id(bx_id)
        if element:
            # element.find_element(*self.ADD_TO_CART_BUTTON).click()
            add_button = element.find_element(*self.ADD_TO_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", add_button)
            return True
        return False

    @allure.step("Нажимаем кнопку перехода на следующую страницу")
    def go_to_next_page(self):
        """Перейти на следующую страницу"""
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXT_PAGE_BUTTON)
            )
            if "disabled" in next_button.get_attribute("class"):
                return False
            next_button.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "catalog"))
            )
            return True
        except Exception:
            return False

    @allure.step("Ищем товар переходя по страницам")
    def find_product_by_id_with_pagination(self, bx_id, max_pages=10):
        """Поиск товара по ID с переключением страниц"""
        for page in range(1, max_pages + 1):
            element = self.find_product_by_id(bx_id)

            if element:
                return element

            if page < max_pages and self.go_to_next_page():
                continue
            else:
                break

        return None

    @allure.step("Находим и добавляем товар в корзину по bx_id с поиском по страницам")
    def add_product_to_cart_by_id_with_pagination(self, bx_id, max_pages=10):
        """Добавить товар в корзину по 'bx_id' с поиском по всем страницам"""
        element = self.find_product_by_id_with_pagination(bx_id, max_pages)

        if element:
            add_button = element.find_element(*self.ADD_TO_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", add_button)
            return True
        return False

    def open_product_card_with_pagination(self, bx_id, max_pages=10):
        """Открытие карточки товара"""
        element = self.find_product_by_id_with_pagination(bx_id, max_pages)
        element.find_element(By.TAG_NAME, "a").click()

    def add_in_favorites(self, bx_id, max_pages):
        """Нажать кнопку 'Добавить в избранное'"""
        element = self.find_product_by_id_with_pagination(bx_id, max_pages)
        checkbox = element.find_element(By.XPATH, ".//input[@type='checkbox']")
        self.driver.execute_script("arguments[0].click();", checkbox)

    def add_multiple_to_favorites(self, products_list, max_pages=10):
        """Добавить несколько товаров в избранное"""
        for bx_id in products_list:
            self.add_in_favorites(bx_id, max_pages)

