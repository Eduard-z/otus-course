from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class OpencartHeaderElement(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "a[title='My Account']")
    REGISTER_USER_LINK_REL = (By.XPATH, "//following-sibling::ul//a[text()='Register']")
    LOGIN_AS_USER_LINK_REL = (By.XPATH, "//following-sibling::ul//a[text()='Login']")
    LOGOUT_LINK_REL = (By.XPATH, "//following-sibling::ul//a[text()='Logout']")
    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    CART_BUTTON = (By.CSS_SELECTOR, "a[title='Shopping Cart']")
    CART_DROPDOWN = (By.CSS_SELECTOR, "#cart button")
    OPENCART_LOGO_LINK = (By.CSS_SELECTOR, "[id='logo'] > a")
    CURRENCY_DROPDOWN = (By.XPATH, "//button/span[text()= 'Currency']/ancestor::button")
    CURRENCY_ICON = (By.XPATH, "//button/span[text()= 'Currency']/preceding-sibling::strong")
    EUR_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='EUR']")
    GBP_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='GBP']")
    USD_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='USD']")

    def expand_my_account_dropdown(self):
        self._click(self.MY_ACCOUNT_DROPDOWN)

    def click_register_account(self):
        self._click_child_element(self.MY_ACCOUNT_DROPDOWN, self.REGISTER_USER_LINK_REL)

    def click_login_into_user_account(self):
        self._click_child_element(self.MY_ACCOUNT_DROPDOWN, self.LOGIN_AS_USER_LINK_REL)

    def is_user_logged_in(self) -> bool:
        try:
            self._verify_element_presence(self.LOGOUT_LINK_REL)
        except AssertionError:
            return False
        return True

    def click_logout(self):
        self._click_child_element(self.MY_ACCOUNT_DROPDOWN, self.LOGOUT_LINK_REL)

    def delete_session_cookie(self):
        self._delete_cookie("OCSESSID")

    def input_text_into_search_field(self, search_text: str):
        self._input_field_value(self.SEARCH_FIELD, search_text)

    def click_search_button(self):
        self._click(self.SEARCH_BUTTON)

    def click_cart_button(self):
        self._click(self.CART_BUTTON)

    def expand_cart_dropdown(self):
        self._click(self.CART_DROPDOWN)

    def click_your_store_link(self):
        self._click(self.OPENCART_LOGO_LINK)

    def expand_currency_dropdown(self):
        self._click(self.CURRENCY_DROPDOWN)
        return self

    def select_currency(self, currency_value: str):
        """Select currency from currency drop-down and verify value selected"""
        if currency_value == "EUR":
            self._select_dropdown_item(self.EUR_CURRENCY_ITEM)
            self._verify_text_in_element(self.CURRENCY_ICON, "€")
        elif currency_value == "GBP":
            self._select_dropdown_item(self.GBP_CURRENCY_ITEM)
            self._verify_text_in_element(self.CURRENCY_ICON, "£")
        elif currency_value == "USD":
            self._select_dropdown_item(self.USD_CURRENCY_ITEM)
            self._verify_text_in_element(self.CURRENCY_ICON, "$")
        else:
            raise AssertionError(f"{currency_value} currency is not supported")
