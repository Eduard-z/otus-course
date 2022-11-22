from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-header h1")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "[id='menu']")
    CATALOG_SECTION = (By.XPATH, "//*[@id='menu-catalog']/a")

    page_title = "Dashboard"

    def ensure_page_is_proper(self, page_header_text):
        page_header = self._verify_element_presence(self.PAGE_HEADER)
        assert page_header.text == page_header_text, f"Page header is not {page_header_text}"

    def check_admin_page_title(self, title=page_title):
        self._verify_page_title(title)

    def wait_until_menu_is_displayed(self):
        self._verify_element_presence(self.NAVIGATION_MENU)

    def open_products_list(self, menu_sub_item_name: str):
        self._click(self.CATALOG_SECTION)
        self._click_child_element(self.CATALOG_SECTION, (By.XPATH, f"//..//a[text()='{menu_sub_item_name}']"))
