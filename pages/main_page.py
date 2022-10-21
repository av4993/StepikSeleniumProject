from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .product_page import ProductPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
            