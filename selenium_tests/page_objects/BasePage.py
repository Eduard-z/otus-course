import logging
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


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

    def _verify_element_presence(self, locator: tuple) -> WebElement:
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

    def _click(self, element: tuple | WebElement):
        """element is either a locator (text) or an WebElement"""
        with allure.step(f'Click element "{element}"'):
            self.logger.info('Click element "%s"', element)

        try:
            WebDriverWait(driver=self.browser, timeout=1).until(EC.element_to_be_clickable(element)).click()
        except TimeoutException:
            self.logger.exception("Exception occurred: Element '%s' not found", element)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Can't find element by locator: {element}")

    def _click_child_element(self, element: tuple | WebElement, relative_locator: tuple):
        """element is either a locator (text) or an WebElement"""
        with allure.step(f'Click element "{relative_locator}"'):
            self.logger.info('Click element "%s"', relative_locator)

        try:
            main_element = element
            if isinstance(element, tuple):
                main_element = self._verify_element_presence(element)
            child_element = main_element.find_element(*relative_locator)
            self._click(child_element)
        except NoSuchElementException:
            self.logger.exception("Exception occurred: Element '%s' not found", relative_locator)
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Can't find element by locator: {relative_locator}")

    def _click_social_net_widget(self, iframe_locator: tuple, locator: tuple):
        with allure.step(f'Click "{locator}" social network share widget'):
            self.logger.info('Click "%s" social network share widget', locator)

            self._switch_to_iframe(iframe_locator)
            widget = self._verify_element_presence(locator)
            ActionChains(self.browser).pause(0.3) \
                .move_to_element(widget).pause(0.9).click_and_hold().pause(0.7).release().perform()

    def _switch_to_iframe(self, iframe_locator: tuple):
        with allure.step(f'Switch to iFrame "{iframe_locator}"'):
            self.logger.info('Switch to iFrame "%s"', iframe_locator)

            try:
                WebDriverWait(driver=self.browser, timeout=3).until(
                    EC.frame_to_be_available_and_switch_to_it(iframe_locator))
            except TimeoutException:
                self.logger.exception("Exception occurred: iFrame '%s' not found", iframe_locator)
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_iFrame_not_found",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Can't find iFrame by locator: {iframe_locator}")

    def _switch_out_of_iframe(self):
        with allure.step('Switch out of iframe to default context'):
            self.logger.info('Switch out of iframe to default context')
            self.browser.switch_to.default_content()

    def _verify_iframe_button_colour(self, iframe_locator: tuple, locator: tuple, colour: str):
        with allure.step(f'Verify "{locator}" button colour inside iframe is {colour}'):
            self.logger.info('Verify "%s" button colour inside iframe is %s', locator, colour)

            self._switch_to_iframe(iframe_locator)
            actual_colour = self._verify_element_presence(locator).value_of_css_property("background-color")
            try:
                assert actual_colour == colour, f"Expected colour to be '{colour}' but it is '{actual_colour}'"
                self._switch_out_of_iframe()
            except AssertionError:
                self.logger.exception("Exception occurred: button colour is not %s", colour)
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_wrong_button_colour",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError(f"Button colour is not {colour}")

    def _verify_page_title(self, page_title: str):
        with allure.step(f'Verify Page Title text is "{page_title}"'):
            self.logger.info('Verify Page Title text is "%s"', page_title)

            actual_title = self.browser.title
            try:
                WebDriverWait(driver=self.browser, timeout=1).until(EC.title_is(page_title))
            except TimeoutException:
                self.logger.exception("Exception occurred: Wrong page title '%s'", actual_title)
                raise AssertionError(f"Expected title to be '{page_title}' but it is '{actual_title}'")

    def _get_browser_current_window_name(self) -> str:
        return self.browser.current_window_handle

    def _get_browser_all_windows(self) -> list:
        return self.browser.window_handles

    def _get_new_window_name(self, old_windows: list) -> str:
        """expected there is 1 new window / tab appeared"""
        old_windows_list = set(old_windows)
        new_windows_list = self._get_browser_all_windows()
        [new_window_name] = [i for i in new_windows_list if i not in old_windows_list]
        return new_window_name

    def _switch_to_another_browser_tab(self, browser_window_handle: str):
        with allure.step(f"Switch to browser tab {browser_window_handle}"):
            self.logger.info("Switch to browser tab %s", browser_window_handle)

            self.browser.switch_to.window(browser_window_handle)

    def _verify_new_window_is_open(self, old_windows: list) -> bool:
        with allure.step('Verify new browser tab is opened'):
            self.logger.info('Verify new browser tab is opened')
            try:
                return WebDriverWait(driver=self.browser, timeout=4).until(
                    EC.new_window_is_opened(old_windows))
            except TimeoutException:
                self.logger.exception("Exception occurred: browser tab not opened")
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="screenshot_browser_tab_not_found",
                    attachment_type=allure.attachment_type.PNG
                )
                raise AssertionError("Can't find browser tab")

    def _delete_cookie(self, cookie_name: str):
        with allure.step(f"Delete cookie '{cookie_name}'"):
            self.logger.info("Delete cookie '%s'", cookie_name)

            self.browser.delete_cookie(cookie_name)
