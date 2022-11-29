from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .BasePage import BasePage


class ShoppingCartPage(BasePage):
    PRODUCT = (By.CSS_SELECTOR, "#content form tbody tr")
    PRODUCT_NAME_REL = (By.CSS_SELECTOR, "td:nth-of-type(2) > a")
    REMOVE_BUTTON_REL = (By.CSS_SELECTOR, "td:nth-of-type(4) button[data-original-title='Remove']")
    CART_EMPTY_STATEMENT = (By.CSS_SELECTOR, "#content p")

    path = "/index.php?route=checkout/cart"
    page_title = "Shopping Cart"

    def check_cart_page_title(self, title=page_title):
        self._verify_page_title(title)

    @property
    def all_products_in_cart(self) -> list[WebElement]:
        return self.browser.find_elements(*self.PRODUCT)

    @property
    def all_product_names_elements(self) -> list[WebElement]:
        return [i.find_element(*self.PRODUCT_NAME_REL) for i in self.all_products_in_cart]

    @property
    def all_product_names(self) -> list:
        return [i.text for i in self.all_product_names_elements]

    def click_remove_button(self):
        self._click_child_element(self.PRODUCT, self.REMOVE_BUTTON_REL)

    def check_cart_empty_statement(self):
        self._verify_text_in_element(self.CART_EMPTY_STATEMENT, "Your shopping cart is empty!")
