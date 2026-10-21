import pytest
from works_flows.web_login_flows import WebLoginFlows


@pytest.mark.usefixtures("init_web_driver")
class TestLoginUI:
    def test_login(self):
        WebLoginFlows.open_login_page()
        WebLoginFlows.login()
        assert WebLoginFlows.is_main_page_displayed()

