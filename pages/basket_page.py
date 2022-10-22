from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "В корзине что то есть, а не должно!"    
    
    def should_be_message_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text, "Корзина не пуста, а должна!"
    
