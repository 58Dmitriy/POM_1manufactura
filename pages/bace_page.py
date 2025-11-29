from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
import random
from typing import List, Dict, Tuple


class BasePage(object):
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

    # Селекторы для выбора рандомного товара
    PRODUCT_ITEM = (By.CSS_SELECTOR, "div.catalog__item")
    PRODUCT_ID = (By.CSS_SELECTOR, "div.catalog__item[id^='bx_']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product__description")
    DATA_ID = "data-id"  # Атрибут с ID товара

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        allure.attach("✅", name="Скролл выполнен", attachment_type=AttachmentType.TEXT)

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)
        allure.attach("✅", name="Страница открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Делаем клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        allure.attach("✅", name="Клик выполнен", attachment_type=AttachmentType.TEXT)

    @allure.step("Вводим текста '{text}'")
    def type(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        allure.attach("✅", name="Текст введен", attachment_type=AttachmentType.TEXT)

    @allure.step("Получаем текст элемента")
    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        result = element.text
        allure.attach(result, name="Текст элемента", attachment_type=AttachmentType.TEXT)
        return result


    BACK_BUTTON = (By.XPATH, "//a[@class='back']") # кнопка "назад"
    NEXT_PAGE_BUTTON = (By.XPATH, "//a[@class='pagination__arrow pagination__arrow--next']") # кнопка перехода на следующую страницу

    CATALOG_ITEM = "//div[@class='catalog']/child::div[@id='{bx_id}']" # товар в каталоге
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(@class, 'js-add-to-basket')]")  # кнопка "Добавить в корзину"
    FAVORITES_BUTTON = (By.XPATH, ".//input[@type='checkbox']") # кнопка добавления в избранное

    @allure.step("Находим товар по bx_id")
    def find_product_by_id(self, bx_id):
        try:
            locator = (By.XPATH, self.CATALOG_ITEM.format(bx_id=bx_id))
            elements = self.driver.find_elements(*locator)
            result = elements[0] if elements else None
            status = "Найден" if result else "Не найден"
            allure.attach(status, name="Результат поиска", attachment_type=AttachmentType.TEXT)
            return result
        except:
            allure.attach("Ошибка поиска", name="Результат поиска", attachment_type=AttachmentType.TEXT)
            return None

    @allure.step("Находим и добавить товар в корзину по bx_id")
    def add_product_to_cart_by_id(self, bx_id):
        element = self.find_product_by_id(bx_id)
        if element:
            add_button = element.find_element(*self.ADD_TO_CART_BUTTON)
            self.scroll_to_element(add_button)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(add_button))
            add_button.click()
            allure.attach("✅", name="Товар добавлен", attachment_type=AttachmentType.TEXT)
            return True
        else:
            allure.attach("❌", name="Товар не найден", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Нажимаем кнопку перехода на следующую страницу")
    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXT_PAGE_BUTTON)
            )
            if "disabled" in next_button.get_attribute("class"):
                allure.attach("❌", name="Кнопка неактивна", attachment_type=AttachmentType.TEXT)
                return False
            next_button.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "catalog"))
            )
            allure.attach("✅", name="Переход выполнен", attachment_type=AttachmentType.TEXT)
            return True
        except Exception:
            allure.attach("❌", name="Ошибка перехода", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Ищем товар переходя по страницам")
    def find_product_by_id_with_pagination(self, bx_id, max_pages=10):
        for page in range(1, max_pages + 1):
            element = self.find_product_by_id(bx_id)

            if element:
                allure.attach(f"✅ Найден на странице {page}", name="Результат поиска",
                              attachment_type=AttachmentType.TEXT)
                return element

            if page < max_pages and self.go_to_next_page():
                allure.attach(f"📄 Страница {page}", name="Переход", attachment_type=AttachmentType.TEXT)
                continue
            else:
                allure.attach(f"❌ Не найден за {page} страниц", name="Результат поиска",
                              attachment_type=AttachmentType.TEXT)
                break

        return None

    @allure.step("Ищем и добавляем товар в корзину по bx_id с поиском по страницам")
    def add_product_to_cart_by_id_with_pagination(self, bx_id, max_pages=10):
        element = self.find_product_by_id_with_pagination(bx_id, max_pages)

        if element:
            add_button = element.find_element(*self.ADD_TO_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", add_button)
            allure.attach("✅", name="Товар добавлен в корзину", attachment_type=AttachmentType.TEXT)
            return True

        allure.attach("❌", name="Товар не найден", attachment_type=AttachmentType.TEXT)
        return False

    @allure.step("Открываем карточку товара")
    def open_product_card_with_pagination(self, bx_id, max_pages=10):
        element = self.find_product_by_id_with_pagination(bx_id, max_pages)
        element.find_element(By.TAG_NAME, "a").click()
        allure.attach("✅", name="Карточка товара открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Нажимаем кнопку 'Добавить в избранное'")
    def add_in_favorites(self, bx_id, max_pages):
        element = self.find_product_by_id_with_pagination(bx_id, max_pages)
        checkbox = element.find_element(By.XPATH, ".//input[@type='checkbox']")
        self.scroll_to_element(checkbox)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(checkbox))
        checkbox.click()
        allure.attach("✅", name="Добавлено в избранное", attachment_type=AttachmentType.TEXT)

    @allure.step("Добавляем несколько товаров в избранное")
    def add_multiple_to_favorites(self, products_list, max_pages=10):
        for bx_id in products_list:
            self.add_in_favorites(bx_id, max_pages)
            allure.attach(f"✅ {bx_id}", name="Товар добавлен", attachment_type=AttachmentType.TEXT)

        allure.attach(f"✅ Всего: {len(products_list)}", name="Итог", attachment_type=AttachmentType.TEXT)

    @allure.step("Собираем список всех товаров на странице")
    def get_products_list(self) -> List[Dict[str, str]]:
        """Собирает список всех товаров на странице
        Возвращает:
            List словарей с id и названием товаров"""
        products = []

        try:
            # Ждем появления товаров на странице
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.PRODUCT_ITEM)
            )

            # Находим все элементы товаров
            product_elements = self.driver.find_elements(*self.PRODUCT_ITEM)

            for product_element in product_elements:
                try:
                    # Извлекаем ID из атрибута id
                    product_id = product_element.get_attribute("id")

                    # Извлекаем название товара
                    name_element = product_element.find_element(*self.PRODUCT_NAME)
                    product_name = name_element.text.strip()

                    # Добавляем в список, если все данные есть
                    if product_id and product_name:
                        products.append({
                            'bx_id': product_id,
                            'product_name': product_name
                        })

                except Exception as e:
                    print(f"Ошибка при извлечении данных товара: {e}")
                    continue

            allure.attach(f"✅ Найдено: {len(products)}", name="Результат сбора", attachment_type=AttachmentType.TEXT)

            # Добавляем детальный список товаров
            if products:
                products_text = "\n".join([f"{p['bx_id']}: {p['product_name']}" for p in products])
                allure.attach(products_text, name="Список товаров", attachment_type=AttachmentType.TEXT)

        except Exception as e:
            allure.attach(f"❌ Ошибка: {str(e)}", name="Результат сбора", attachment_type=AttachmentType.TEXT)
            print(f"Ошибка при поиске товаров: {e}")

        return products

    @allure.step("Выбираем случайный товар из каталога")
    def get_random_product(self) -> Tuple[str, str]:
        """Выбирает случайный товар из списка
        Возвращает:
            Кортеж (id, название) случайного товара"""
        products = self.get_products_list()

        if not products:
            allure.attach("❌", name="Товары не найдены", attachment_type=AttachmentType.TEXT)
            raise ValueError("На странице не найдено товаров")

        random_product = random.choice(products)
        allure.attach(f"{random_product['bx_id']}: {random_product['product_name']}",
                      name="Выбранный товар", attachment_type=AttachmentType.TEXT)
        return random_product['bx_id'], random_product['product_name']
