from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ..BasePage import BasePage


class ProductCardElement(BasePage):
    PRODUCT_CARD = (By.CSS_SELECTOR, ".product-thumb")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption a")

    @property
    def all_product_cards_elements(self) -> list[WebElement]:
        return self.browser.find_elements(*self.PRODUCT_CARD)

    @property
    def all_product_names_elements(self) -> list[WebElement]:
        return [i.find_element(*self.PRODUCT_NAME) for i in self.all_product_cards_elements]

    @property
    def all_product_names(self) -> list:
        return [i.text for i in self.all_product_names_elements]
