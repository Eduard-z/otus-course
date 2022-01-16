from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input[name='product_id'] ~ button")
    BREADCRUMB_ITEM = (By.CSS_SELECTOR, ".breadcrumb a")
    PRODUCT_IMAGE_ADDITIONAL = (By.CSS_SELECTOR, ".image-additional")
    PRODUCT_INFO_ACTIVE_TAB = (By.CSS_SELECTOR, ".active > a")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR,
                              ".btn-group > button[data-original-title='Add to Wish List']")
    QTY_FIELD = (By.CSS_SELECTOR, "[name='quantity']")

    path = "/index.php?route=product/product&product_id=43"

    def open_product_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def find_add_to_cart_button(self):
        self._verify_element_presence(self.ADD_TO_CART_BUTTON)

    def find_breadcrumb_item(self):
        self._verify_element_presence(self.BREADCRUMB_ITEM)

    def find_product_image_additional(self):
        self._verify_element_presence(self.PRODUCT_IMAGE_ADDITIONAL)

    def find_product_info_active_tab(self):
        self._verify_element_presence(self.PRODUCT_INFO_ACTIVE_TAB)

    def find_add_to_wishlist_button(self):
        self._verify_element_presence(self.ADD_TO_WISHLIST_BUTTON)

    def find_qty_field(self):
        self._verify_element_presence(self.QTY_FIELD)
