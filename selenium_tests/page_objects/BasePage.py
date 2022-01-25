import logging
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)

        self.log_file = logging.FileHandler(
            f"selenium_tests/logs/{self.browser.test_name}.log", mode="a")
        self.format_logs = logging.Formatter(
            "%(asctime)s.%(msecs)d %(levelname)s %(name)s: %(filename)s:%(lineno)d '%(message)s'",
            datefmt="%d-%b-%Y %H:%M:%S")

        self.log_file.setFormatter(self.format_logs)
        self.logger.addHandler(self.log_file)
        self.logger.setLevel(level=self.browser.log_level)

    def _verify_element_presence(self, locator: tuple):
        with allure.step(f'Verify element "{locator}" is present'):
            self.logger.info('Verify element "%s" is present', locator)

            try:
                return WebDriverWait(driver=self.browser, timeout=2) \
                    .until(EC.presence_of_element_located(locator))
            except TimeoutException:
                self.logger.exception("Exception occurred")
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_element_not_found",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Can't find element by locator: {locator}")

    def _verify_text_in_element(self, locator: tuple, element_text):
        with allure.step(f'Verify text "{element_text}" is present in element "{locator}"'):
            self.logger.info('Verify text "%s" in element "%s"', element_text, locator)

            try:
                WebDriverWait(driver=self.browser, timeout=3) \
                    .until(EC.text_to_be_present_in_element(locator, element_text))
            except TimeoutException:
                self.logger.exception("Exception occurred")
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_text_not_match",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Expected text to be '{element_text}' "
                                     f"but it is '{self.browser.find_element(*locator).text}'")

    def _input_field_value(self, field_locator: tuple, field_value):
        with allure.step(f'Input value "{field_value}" into field "{field_locator}"'):
            self.logger.info('Input value "%s" into field "%s"', field_value, field_locator)
            input_field = self._verify_element_presence(field_locator)
            input_field.click()
            input_field.clear()
            input_field.send_keys(field_value)

    def _select_dropdown_item(self, locator: tuple):
        with allure.step(f'Select "{locator}" item from dropdown'):
            self.logger.info('Select "%s" item from dropdown', locator)
            dropdown_element = self._verify_element_presence(locator)
            ActionChains(self.browser).pause(0.3) \
                .move_to_element(dropdown_element).click().perform()
