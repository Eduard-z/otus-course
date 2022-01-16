from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserAccountCreatedPage(BasePage):
    CONGRATULATIONS_HEADING = (By.CSS_SELECTOR, "#content > h1")

    def check_success_message(self):
        success_message = self._verify_element_presence(self.CONGRATULATIONS_HEADING).text
        assert success_message == "Your Account Has Been Created!"
