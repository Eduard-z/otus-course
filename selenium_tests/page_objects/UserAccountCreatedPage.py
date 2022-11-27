from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserAccountCreatedPage(BasePage):
    CONGRATULATIONS_HEADING = (By.CSS_SELECTOR, "#content > h1")

    page_title = "Your Account Has Been Created!"

    def check_user_account_page_title(self, title=page_title):
        self._verify_page_title(title)

    def check_success_message(self):
        success_message = self._verify_element_presence(self.CONGRATULATIONS_HEADING).text
        assert success_message == "Your Account Has Been Created!"
