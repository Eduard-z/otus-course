from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class CatalogProductsPage(BasePage):
    SUCCESS_ALERT = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    FILTER_PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "input[name='filter_name']")
    FILTER_BUTTON = (By.CSS_SELECTOR, "button#button-filter")
    PRODUCT_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name='selected[]']")
    NAME_OF_PRODUCT_IN_THE_LIST = (By.CSS_SELECTOR, "tbody > tr > td:nth-of-type(3)")

    def check_success_alert_displayed(self):
        self._verify_element_presence(self.SUCCESS_ALERT)

    def filter_products_by_name(self, product_name):
        product_name_field = self._verify_element_presence(self.FILTER_PRODUCT_NAME_FIELD)
        product_name_field.click()
        product_name_field.clear()
        product_name_field.send_keys(product_name)
        self.browser.find_element(*self.FILTER_BUTTON).click()

    def select_first_product(self):
        self.browser.find_element(*self.PRODUCT_CHECKBOX).click()

    def number_of_products_filtered_by_name(self, product_name):
        all_products_displayed = self.browser.find_elements(*self.NAME_OF_PRODUCT_IN_THE_LIST)
        number_of_products_filtered = 0
        for i in all_products_displayed:
            if i.text == product_name:
                number_of_products_filtered += 1

        return number_of_products_filtered
