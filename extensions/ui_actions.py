import allure
from test_cases import conftest as conf



class UIActions:
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

