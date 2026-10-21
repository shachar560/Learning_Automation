import allure
from extensions.ui_actions import UIActions
from page_objects import login_page
from utilities.common_ops import get_data


class WebLoginFlows:
    @staticmethod
    @allure.step("Open Login Page")
    def open_login_page():
        UIActions.open_url(get_data("SauceDemo_Login_url"))

    @staticmethod
    @allure.step("Login with optional custom Username and Password")
    def login(username=None, password=None):
        active_username = username if username is not None else get_data("SauceDemo_UserName")
        active_password = password if password is not None else get_data("SauceDemo_Password")

        UIActions.update_text(login_page.user_name_field, active_username)
        UIActions.update_text(login_page.password_field, active_password)
        UIActions.click(login_page.login_button)

    @staticmethod
    @allure.step("Get Login Error Message")
    def get_error_message():
        return UIActions.get_text(login_page.error_message)

    @staticmethod
    @allure.step("Check if Main Page is Displayed")
    def is_main_page_displayed():
        return UIActions.wait_for_url_contains("/inventory")