from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_SHOW_BASKET = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
       
class MainPageLocators():
    pass

class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "div.register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_FIELD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-lg")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")