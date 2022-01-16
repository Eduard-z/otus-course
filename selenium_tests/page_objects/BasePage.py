from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(driver=self.browser, timeout=2) \
                .until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator: {locator}")

    def _verify_text_in_element(self, locator: tuple, element_text):
        try:
            WebDriverWait(driver=self.browser, timeout=3) \
                .until(EC.text_to_be_present_in_element(locator, element_text))
        except TimeoutException:
            raise AssertionError(f"Expected text to be '{element_text}' "
                                 f"but it is '{self.browser.find_element(*locator).text}'")

    def _input_field_value(self, field_locator: tuple, field_value):
        input_field = self._verify_element_presence(field_locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(field_value)

    def _select_dropdown_item(self, locator: tuple):
        dropdown_element = self._verify_element_presence(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(dropdown_element).click().perform()
