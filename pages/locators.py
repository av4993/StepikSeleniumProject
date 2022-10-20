from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "div.register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")

    