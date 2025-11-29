from selenium.webdriver.common.by import By
from pages.bace_page import BasePage
import allure
from allure_commons.types import AttachmentType


class HeaderPage(BasePage):

    """Header страниц (sub навигационное меню)"""
    COMPANY = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Компания'][1]") # ссылка "Компания"
    WHOLESALERS = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Оптовикам'][1]") # ссылка "Оптовикам"
    BLOG = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Блог'][1]") # ссылка "Блог"
    CONTACTS = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Контакты'][1]") # ссылка "Контакты"
    # PROMOTIONS = (By.XPATH, "")
    PAYMENT = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Оплата'][1]") # ссылка "Оплата"
    DELIVERY = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Доставка'][1]") # ссылка "Доставка"
    HELP = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Помощь'][1]") # ссылка "Помощь"
    PERSONAL_ACCOUNT = (By.XPATH, "//div[@class='wrap-layer']/following::a[text()='Личный кабинет") # ссылка "Личный кабинет"

    """Header страниц (центральный)"""
    FAVORITES_BUTTON = (By.XPATH, "//a[@class='favorites']") # кнопка "Избранное"
    FAVORITES_COUNTER = (By.XPATH, "") # счётчик товаров в избранном
    CART_BUTTON = (By.XPATH, "//a[@class='cart']") # кнопка "Корзина"
    CART_COUNTER = (By.XPATH, "//a[@class='cart']/following::div[@class='data-small']") # счётчик корзины товара
    COMPARISON_BUTTON = (By.XPATH, "//a[@class='compare']") # кнопка "Сравнение"
    SEARCH_BUTTON = (By.XPATH, "//button[@id='btn-search-header']") # кнопка "Поиск"

    """Навигационное меню"""
    HORSEMEN = (By.XPATH, "//a[@class='nav-main__link' and text()='Всадникам']") # Раздел "Всадникам"
    HORSES = (By.XPATH, "//a[@class='nav-main__link' and text()='Лошадям']") # Раздел "Лошадям"
    DISCOUNTED_PRODUCTS = (By.XPATH, "//a[@class='nav-main__link' and text()='Товары с уценкой']") # Раздел "Товары с уценкой"
    STABLE = (By.XPATH, "//a[@class='nav-main__link' and text()='Конюшня']") # Раздел "Конюшня"
    FEEDING_AND_CARE = (By.XPATH, "//a[@class='nav-main__link' and text()='Подкормки, уход']") # Раздел "Подкормки, уход"
    CERTIFICATES = (By.XPATH, "//a[@class='nav-main__link' and text()='Сертификаты']") # Раздел "Сертификаты"
    FOR_DOGS = (By.XPATH, "//a[@class='nav-main__link' and text()='Собакам']") # Раздел "Собакам"
    BRANDING = (By.XPATH, "//a[@class='nav-main__link' and text()='Брендирование']") # Раздел "Брендирование"
    DISCOUNTS = (By.XPATH, "//a[@class='nav-main__link' and text()='Скидки']") # Раздел "Скидки"
    NEW = (By.XPATH, "//a[@class='nav-main__link' and text()='Новинки']") # Раздел "Новинки"
    BRANDS = (By.XPATH, "//a[@class='nav-main__link' and text()='Бренды']") # Раздел "Бренды"

    @allure.step("Открываем главную страницу")
    def open_home_page(self):
        self.open("https://1manufactura.ru/")
        allure.attach("✅", name="Главная страница открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Переходим в раздел 'Избранное'")
    def go_to_favorites_page(self):
        self.driver.find_element(*self.FAVORITES_BUTTON).click()
        allure.attach("✅", name="Раздел открыт", attachment_type=AttachmentType.TEXT)

    @allure.step("Переходим в корзину товаров")
    def go_to_cart_page(self):
        self.driver.find_element(*self.CART_BUTTON).click()
        allure.attach("✅", name="Корзина открыта", attachment_type=AttachmentType.TEXT)

    @allure.step("Переходим в каталог 'Всадникам'")
    def go_to_vsadnikam_page(self):
        self.driver.find_element(*self.HORSEMEN).click()
        allure.attach("✅", name="Каталог открыт", attachment_type=AttachmentType.TEXT)

    @allure.step("Переходим в каталог 'Лошадям'")
    def go_to_horses_page(self):
        self.driver.find_element(*self.HORSES).click()
        allure.attach("✅", name="Каталог открыт", attachment_type=AttachmentType.TEXT)

    @allure.step("Переходим в каталог 'Конюшня'")
    def go_to_stable_page(self):
        self.driver.find_element(*self.STABLE).click()
        allure.attach("✅", name="Каталог открыт", attachment_type=AttachmentType.TEXT)

    @allure.step("Проверяем отображается ли счётчик корзины")
    def cart_counter_is_displayed(self):
        try:
            counter = self.driver.find_element(*self.CART_COUNTER)
            result = counter.is_displayed()
            status = "✅ Отображается" if result else "❌ Не отображается"
            allure.attach(status, name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return result
        except:
            allure.attach("❌ Элемент не найден", name="Результат проверки", attachment_type=AttachmentType.TEXT)
            return False

    @allure.step("Проверяем чему равен счётчик корзины")
    def cart_counter(self):
        if self.cart_counter_is_displayed():
            count_text = self.get_text(self.CART_COUNTER)
            result = int(count_text)
            allure.attach(str(result), name="Значение счетчика", attachment_type=AttachmentType.TEXT)
            return result

        allure.attach("0", name="Значение счетчика", attachment_type=AttachmentType.TEXT)
        return 0