import pytest
from selenium import webdriver
from utilities.common_ops import get_data

driver = None

@pytest.fixture(scope="class")
def init_web_driver(request):
    global driver

    driver = get_web_driver()
    driver.maximize_window()
    driver.implicitly_wait(int(get_data("WaitTime")))
    driver.get(get_data("SauceDemo_Login_url"))

    request.cls.driver = driver
    yield driver
    driver.quit()


def get_web_driver():
    browser = get_data("Browser")
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        # כיבוי מנהל הסיסמאות של Chrome - כדי שלא יקפוץ חלון שמירת סיסמה או אימות של Windows אחרי הלוגין
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        # מ-Selenium 4.6 ומעלה אין צורך להוריד ChromeDriver - Selenium מוריד אותו לבד
        return webdriver.Chrome(options=options)
    elif browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        # Edge בנוי על אותו מנוע של Chrome - לכן אותן הגדרות לכיבוי מנהל הסיסמאות
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        # גם כאן Selenium מוריד את EdgeDriver לבד
        return webdriver.Edge(options=options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        # כיבוי ההצעה של Firefox לשמור סיסמה אחרי הלוגין
        options.set_preference("signon.rememberSignons", False)
        # גם כאן Selenium מוריד את GeckoDriver (הדרייבר של Firefox) לבד
        return webdriver.Firefox(options=options)
    else:
        raise Exception("Browser '" + browser + "' is not supported. Supported browsers: Chrome, Edge, Firefox")