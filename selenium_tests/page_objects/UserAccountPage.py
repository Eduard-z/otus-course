from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserAccountPage(BasePage):
    BREADCRUMB_ACCOUNT = (By.CSS_SELECTOR, ".breadcrumb li:last-child a")

    path = "/index.php?route=account/account"
    page_title = "My Account"
    breadcrumb = "Account"

    def check_user_account_page_title(self, title=page_title):
        self._verify_page_title(title)

    def check_user_account_breadcrumb(self):
        self._verify_text_in_element(self.BREADCRUMB_ACCOUNT, self.breadcrumb)
