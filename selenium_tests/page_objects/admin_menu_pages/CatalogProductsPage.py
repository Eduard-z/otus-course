from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class CatalogProductsPage(BasePage):
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    SUCCESS_ALERT = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    FILTER_PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "input[name='filter_name']")
    FILTER_BUTTON = (By.CSS_SELECTOR, "button#button-filter")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name='selected[]']")
    NAME_OF_PRODUCT_IN_THE_LIST = (By.CSS_SELECTOR, "tbody > tr > td:nth-of-type(3)")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")

    page_title = "Products"

    def check_products_page_title(self, title=page_title):
        self._verify_page_title(title)

    def click_add_new_button(self):
        self._click(self.ADD_NEW_BUTTON)

    def check_success_alert_displayed(self):
        self._verify_element_presence(self.SUCCESS_ALERT)

    def filter_products_by_name(self, product_name: str):
        self._input_field_value(self.FILTER_PRODUCT_NAME_FIELD, product_name)
        self._click(self.FILTER_BUTTON)

    def select_first_product_in_product_list(self):
        self._click(self.PRODUCT_CHECKBOX)

    def number_of_products_filtered_by_name(self, product_name: str) -> int:
        all_products_displayed = self.browser.find_elements(*self.NAME_OF_PRODUCT_IN_THE_LIST)
        return len([i for i in all_products_displayed if i.text == product_name])

    def click_delete_product_button(self):
        self._click(self.DELETE_BUTTON)

    def confirm_product_deleting(self):
        confirm_alert = self.browser.switch_to.alert
        confirm_alert.accept()
