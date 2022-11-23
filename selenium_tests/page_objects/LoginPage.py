from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_FORM = (By.CLASS_NAME, "panel-default")
    USERNAME_FIELD = (By.ID, "input-username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    LINK_TO_OPENCART_SITE = (By.XPATH, "//*[text()='OpenCart']")

    path = "/admin"
    page_title = "Administration"

    def open_login_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def check_login_page_title(self, title=page_title):
        self._verify_page_title(title)

    def wait_until_login_form_is_displayed(self):
        self._verify_element_presence(self.LOGIN_FORM)

    def input_username(self, admin_name: str):
        self._input_field_value(self.USERNAME_FIELD, admin_name)

    def input_password(self, admin_password: str):
        self._input_field_value(self.PASSWORD_FIELD, admin_password)

    def click_login_button(self):
        self._click(self.LOGIN_BUTTON)

    def click_forgotten_password_link(self):
        self._click(self.FORGOTTEN_PASSWORD_LINK)

    def click_link_to_opencart_site(self):
        self._click(self.LINK_TO_OPENCART_SITE)
