from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductCategoryPage(BasePage):
    PAGE_HEADER = (By.CSS_SELECTOR, "#content > h2")

    def check_product_category_page_title(self, title: str):
        self._verify_page_title(title)

    def check_product_category_page_header(self, page_header_text: str):
        page_header = self._verify_element_presence(self.PAGE_HEADER)
        assert page_header.text == page_header_text, f"Page header is not {page_header_text}"
