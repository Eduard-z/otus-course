from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    NAVIGATION_BAR_ITEMS = (By.CSS_SELECTOR, ".navbar-collapse > ul > li > a")
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "a[title='My Account']")
    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-inverse")
    YOUR_STORE_LINK = (By.CSS_SELECTOR, "[id='logo'] > a")
    PRODUCT_ITEM_CARD = (By.CSS_SELECTOR, ".product-layout")
    CURRENCY_DROPDOWN = (By.XPATH, "//button/span[text()= 'Currency']/ancestor::button")
    CURRENCY_ICON = (By.XPATH, "//button/span[text()= 'Currency']/preceding-sibling::strong")
    EUR_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='EUR']")
    GBP_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='GBP']")
    USD_CURRENCY_ITEM = (By.XPATH, "//form[@id='form-currency']//button[@name='USD']")

    MENU_ITEMS_NAMES = ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software',
                        'Phones & PDAs', 'Cameras', 'MP3 Players']

    def open_main_page(self):
        self.browser.get(url=self.browser.url)

    def check_navigation_menu_items_names(self):
        menu_items_names = self.browser.find_elements(*self.NAVIGATION_BAR_ITEMS)
        assert [i.text for i in menu_items_names] == self.MENU_ITEMS_NAMES, \
            f"Wrong items: {menu_items_names} - in Navigation menu"

    def expand_my_account_dropdown(self):
        self._verify_element_presence(self.MY_ACCOUNT_DROPDOWN).click()

    def click_register_account(self):
        self._verify_element_presence(self.MY_ACCOUNT_DROPDOWN) \
            .find_element(By.XPATH, "//following-sibling::ul//a[text()='Register']").click()

    def input_text_into_search_field(self, search_text: str):
        self._input_field_value(self.SEARCH_FIELD, search_text)

    def click_search_button(self):
        self._verify_element_presence(self.SEARCH_BUTTON).click()

    def find_cart_button(self):
        self._verify_element_presence(self.CART_BUTTON)

    def find_your_store_link(self):
        self._verify_element_presence(self.YOUR_STORE_LINK)

    def find_product_item_card(self):
        self._verify_element_presence(self.PRODUCT_ITEM_CARD)

    def expand_currency_dropdown(self):
        self._verify_element_presence(self.CURRENCY_DROPDOWN).click()
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
