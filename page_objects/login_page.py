from selenium.webdriver.common.by import By

user_name_field = (By.ID, "user-name")
password_field = (By.ID, "password")
login_button = (By.ID, "login-button")
error_message = (By.CSS_SELECTOR, "[data-test='error']")
