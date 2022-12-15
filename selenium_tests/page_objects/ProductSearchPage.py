from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductSearchPage(BasePage):
    SEARCH_CRITERIA_FIELD = (By.CSS_SELECTOR, "input[placeholder='Keywords']")
    NO_PRODUCTS_STATEMENT = (By.CSS_SELECTOR, "#content p:last-of-type")

    path = "/index.php?route=product/search"
    page_title_part1 = "Search - "

    def open_search_page(self):
        self.browser.get(url=self.browser.url + self.path)

    def check_search_page_title(self, title_postfix: str, title_prefix=page_title_part1):
        """Page title consists of 'Search - ' and search_text without leading, trailing or extra spaces"""
        page_title_part2 = " ".join(title_postfix.split())
        self._verify_page_title(title_prefix + page_title_part2)

    @property
    def search_criteria_field_value(self):
        return self._verify_element_presence(self.SEARCH_CRITERIA_FIELD).get_attribute("value")

    @property
    def no_product_statement(self):
        return self._verify_element_presence(self.NO_PRODUCTS_STATEMENT).text
