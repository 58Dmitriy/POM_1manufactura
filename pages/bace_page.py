from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        text = self.wait.until(EC.presence_of_element_located(locator))
        return text
