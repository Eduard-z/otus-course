from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .BasePage import BasePage


class MainPage(BasePage):
    NAVIGATION_BAR_ITEMS = (By.XPATH, "//ul[contains(@class, 'navbar-nav')]/li/a")

    MENU_ITEMS_NAMES = ['Desktops', 'Laptops & Notebooks', 'Components', 'Tablets', 'Software',
                        'Phones & PDAs', 'Cameras', 'MP3 Players']
    page_title = "Your Store"

    def open_main_page(self):
        self.browser.get(url=self.browser.url)

    def check_main_page_title(self, title=page_title):
        self._verify_page_title(title)

    @property
    def all_navigation_menu_items_elements(self) -> list[WebElement]:
        return self.browser.find_elements(*self.NAVIGATION_BAR_ITEMS)

    def get_menu_item_element_by_name(self, menu_item: str) -> WebElement:
        return next((i for i in self.all_navigation_menu_items_elements if i.text == menu_item), None)

    def is_item_a_dropdown(self, menu_item: str) -> bool:
        """check whether menu item is dropdown element"""
        menu_item_element = self.get_menu_item_element_by_name(menu_item)
        if menu_item_element.get_attribute("data-toggle") == "dropdown":
            return True

    def check_navigation_menu_items_names(self):
        menu_items_names = self.all_navigation_menu_items_elements
        assert [i.text for i in menu_items_names] == self.MENU_ITEMS_NAMES, \
            f"Wrong items: {menu_items_names} - in Navigation menu"

    def expand_navigation_menu_item_dropdown(self, menu_item: str):
        self._click(self.get_menu_item_element_by_name(menu_item))

    def click_nav_menu_item_inside_dropdown(self, menu_item: str):
        menu_item_element = self.get_menu_item_element_by_name(menu_item)
        self._click_child_element(menu_item_element,
                                  (By.XPATH, f"//following-sibling::div//a[text()='Show All {menu_item}']"))

    def click_nav_menu_item(self, menu_item: str):
        self._click(self.get_menu_item_element_by_name(menu_item))
