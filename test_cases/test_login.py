import pytest
from extensions.ui_actions import UIActions
from page_objects import login_page
from utilities.common_ops import get_data


@pytest.mark.usefixtures("init_web_driver")
class TestLoginUI:
    def test_login(self):
        UIActions.update_text(login_page.user_name_field, get_data("SauceDemo_UserName"))
        UIActions.update_text(login_page.password_field, get_data("SauceDemo_Password"))
        UIActions.click(login_page.login_button)
        assert "inventory" in self.driver.current_url

