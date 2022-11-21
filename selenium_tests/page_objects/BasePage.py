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
            f"selenium_tests/logs/{self.browser.test_name}.log", mode="a", encoding="utf-8")
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
                self.logger.exception("Exception occurred: Element '%s' not found", locator)
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_element_not_found",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Can't find element by locator: {locator}")

    def _verify_text_in_element(self, locator: tuple, element_text: str):
        with allure.step(f'Verify text "{element_text}" is present in element "{locator}"'):
            self.logger.info('Verify text "%s" in element "%s"', element_text, locator)

            try:
                WebDriverWait(driver=self.browser, timeout=3) \
                    .until(EC.text_to_be_present_in_element(locator, element_text))
            except TimeoutException:
                self.logger.exception("Exception occurred: Element '%s' does not contain '%s'", locator, element_text)
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_text_not_match",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Expected text to be '{element_text}' "
                                     f"but it is '{self.browser.find_element(*locator).text}'")

    def _input_field_value(self, field_locator: tuple, field_value: str):
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

    def _click(self, locator: tuple):
        with allure.step(f'Click element "{locator}"'):
            self.logger.info('Click element "%s"', locator)

        try:
            WebDriverWait(driver=self.browser, timeout=1).until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            self.logger.exception("Exception occurred: Element '%s' not found", locator)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Can't find element by locator: {locator}")

    def _click_facebook_like_widget(self, locator: tuple):
        with allure.step(f'Click "{locator}" facebook Like widget'):
            self.logger.info('Click "%s" facebook Like widget', locator)
            dropdown_element = self._verify_element_presence(locator)
            ActionChains(self.browser).pause(0.3) \
                .move_to_element(dropdown_element).pause(1).click_and_hold().pause(1).release().perform()

    def _switch_out_of_iframe(self):
        with allure.step('Switch out of iframe to default context'):
            self.logger.info('Switch out of iframe to default context')
            self.browser.switch_to.default_content()

    def _verify_page_title(self, page_title: str):
        with allure.step(f'Verify Page Title text is "{page_title}"'):
            self.logger.info('Verify Page Title text is "%s"', page_title)
            actual_title = self.browser.title
            try:
                assert actual_title == page_title
            except AssertionError:
                self.logger.exception("Exception occurred: Wrong page title '%s'", actual_title)
                raise AssertionError(f"Wrong page title {actual_title}")

    def _get_browser_current_windows(self):
        main_window = self.browser.current_window_handle
        current_browser_tabs = self.browser.window_handles
        return current_browser_tabs

    def _switch_to_another_browser_tab(self, browser_window_handle):
        self.browser.switch_to.window(browser_window_handle)

    def _verify_new_window_is_open(self, old_windows):
        with allure.step('Verify new browser tab is opened'):
            self.logger.info('Verify new browser tab is opened')
            try:
                WebDriverWait(driver=self.browser, timeout=2)\
                    .until(EC.new_window_is_opened(old_windows))
                return list(set(self.browser.window_handles).difference(set(old_windows)))[0]
            except TimeoutException:
                self.logger.exception("Exception occurred")
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_browser_tab_not_found",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError("Can't find browser tab")
