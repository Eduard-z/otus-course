from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "[id='menu']")
    CATALOG_SECTION = (By.CSS_SELECTOR, "[id='menu-catalog'] > a")
    PRODUCTS_ITEM = (By.XPATH, "//*[@id='menu-catalog']//a[text()='Products']")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")

    def ensure_page_is_proper(self, page_header_text):
        page_header = self._verify_element_presence(self.PAGE_HEADER)
        assert page_header.text == page_header_text

    def wait_until_menu_is_displayed(self):
        self._verify_element_presence(self.NAVIGATION_MENU)

    def open_products_list(self):
        self.browser.find_element(*self.CATALOG_SECTION).click()
        self.browser.find_element(*self.PRODUCTS_ITEM).click()

    def click_add_new_button(self):
        self.browser.find_element(*self.ADD_NEW_BUTTON).click()

    def delete_product(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()
        confirm_alert = self.browser.switch_to.alert
        confirm_alert.accept()
