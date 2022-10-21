from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "div.register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages strong")