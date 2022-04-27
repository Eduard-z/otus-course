from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    NAVIGATION_BAR = (By.CSS_SELECTOR, ".navbar-collapse")
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "a[title='My Account']")
    SEARCH_FIELD = (By.NAME, "search")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-inverse")
    YOUR_STORE_LINK = (By.CSS_SELECTOR, "[id='logo'] > a")
    PRODUCT_ITEM_CARD = (By.CSS_SELECTOR, ".product-layout")
    CURRENCY_DROPDOWN = (By.XPATH, "//button/span[text()= 'Currency']/ancestor::button")
    CURRENCY_ICON = (By.XPATH, "//button/span[text()= 'Currency']/preceding-sibling::strong")
    EUR_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='EUR']")
    GBP_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='GBP']")
    USD_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='USD']")

    def open_main_page(self):
        self.browser.get(url=self.browser.url)

    def find_navigation_bar(self):
        self._verify_element_presence(self.NAVIGATION_BAR)

    def expand_my_account_dropdown(self):
        self._verify_element_presence(self.MY_ACCOUNT_DROPDOWN).click()

    def click_register_account(self):
        self._verify_element_presence(self.MY_ACCOUNT_DROPDOWN) \
            .find_element(By.XPATH, "//following-sibling::ul//a[text()='Register']").click()

    def find_search_field(self):
        self._verify_element_presence(self.SEARCH_FIELD)

    def find_cart_button(self):
        self._verify_element_presence(self.CART_BUTTON)

    def find_your_store_link(self):
        self._verify_element_presence(self.YOUR_STORE_LINK)

    def find_product_item_card(self):
        self._verify_element_presence(self.PRODUCT_ITEM_CARD)

    def expand_currency_dropdown(self):
        self._verify_element_presence(self.CURRENCY_DROPDOWN).click()
        return self

    def select_currency(self, currency_value):
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
