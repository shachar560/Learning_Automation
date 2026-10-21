import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_cases import conftest as conf
from utilities.common_ops import get_data


class UIActions:
    @staticmethod
    @allure.step("Open URL '{url}'")
    def open_url(url):
        conf.driver.get(url)

    @staticmethod
    @allure.step("Click on Element")
    def click(locator):
        conf.driver.find_element(locator[0], locator[1]).click()

    @staticmethod
    @allure.step("Send Text to Element")
    def update_text(locator, text):
        element = conf.driver.find_element(locator[0], locator[1])
        element.clear()
        element.send_keys(text)

    @staticmethod
    @allure.step("Get Text from Element")
    def get_text(locator):
        return conf.driver.find_element(locator[0], locator[1]).text

    @staticmethod
    @allure.step("Wait for URL to contain '{text}'")
    def wait_for_url_contains(text):
        try:
            # מחכה עד WaitTime שניות (מ-data.xml) שהכתובת תכיל את הטקסט
            WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.url_contains(text))
            return True
        except TimeoutException:
            return False

