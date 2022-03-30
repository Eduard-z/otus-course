from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CataloguePage(BasePage):
    CATALOGUE_ITEM_CARD = (By.CSS_SELECTOR, ".product-grid img")
    PRODUCTS_GROUP_MENU_ACTIVE = (By.CSS_SELECTOR, ".list-group .active")
    FILTER_SORTBY_LABEL = (By.XPATH, "//label[text()='Sort By:']")
    ADD_TO_CART_PRODUCT_BUTTON = (By.XPATH, "//button//span[text()='Add to Cart']")
    NUMBER_OF_PRODUCTS_AND_PAGES = (By.XPATH, "//div/div[contains(text(), 'Showing')]")

    path = "/index.php?route=product/category&path=20"

    def open_catalogue_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def find_catalogue_item_card(self):
        self._verify_element_presence(self.CATALOGUE_ITEM_CARD)

    def find_products_group_menu_active(self):
        self._verify_element_presence(self.PRODUCTS_GROUP_MENU_ACTIVE)

    def find_filter_sortby_label(self):
        self._verify_element_presence(self.FILTER_SORTBY_LABEL)

    def find_add_to_cart_product_button(self):
        self._verify_element_presence(self.ADD_TO_CART_PRODUCT_BUTTON)

    def find_number_of_products_and_pages(self):
        self._verify_element_presence(self.NUMBER_OF_PRODUCTS_AND_PAGES)
