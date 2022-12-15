from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginUserPage(BasePage):
    LOGIN_FORM = (By.CSS_SELECTOR, "#content form[action]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    path = "/index.php?route=account/login"
    page_title = "Account Login"

    def open_login_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def check_login_page_title(self, title=page_title):
        self._verify_page_title(title)

    def wait_until_login_form_is_displayed(self):
        self._verify_element_presence(self.LOGIN_FORM)

    def input_email(self, email_address: str):
        self._input_field_value(self.EMAIL_FIELD, email_address)

    def input_password(self, admin_password: str):
        self._input_field_value(self.PASSWORD_FIELD, admin_password)

    def click_login_button(self):
        self._click(self.LOGIN_BUTTON)
