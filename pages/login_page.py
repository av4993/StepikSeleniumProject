from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        mail_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        mail_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REG_PASS_FIELD)
        pass_field.send_keys(password)
        repeat_pass_field = self.browser.find_element(*LoginPageLocators.REG_PASS_FIELD_REPEAT)
        repeat_pass_field.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()
    
    def delete_user(self, password):
        delete1 = self.browser.find_element(*LoginPageLocators.DELETE_BUTTON)   
        delete1.click()
        field_pass1 = self.browser.find_element(*LoginPageLocators.FIELD_PASS_FOR_DELETE)
        field_pass1.send_keys(password) 
        delete2 = self.browser.find_element(*LoginPageLocators.DELETE_BUTTON_FIN)
        delete2.click()
        
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, "Address is not correct!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not found!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "registration form is not found!"
        
        