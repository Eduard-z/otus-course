from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class AlertElement(BasePage):
    ALERT = (By.CSS_SELECTOR, ".alert")

    @property
    def alert_text(self) -> str:
        return self._verify_element_presence(self.ALERT).text
