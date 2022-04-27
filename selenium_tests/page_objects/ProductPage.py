from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input[name='product_id'] ~ button")
    BREADCRUMB_ITEM = (By.CSS_SELECTOR, ".breadcrumb a")
    PRODUCT_IMAGE_ADDITIONAL = (By.CSS_SELECTOR, ".image-additional")
    PRODUCT_INFO_ACTIVE_TAB = (By.CSS_SELECTOR, ".active > a")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR,
                              ".btn-group > button[data-original-title='Add to Wish List']")
    QTY_FIELD = (By.CSS_SELECTOR, "[name='quantity']")
    FACEBOOK_FRAME = (By.CSS_SELECTOR, "#facebook button[title='Like'] span")
    TWITTER_FRAME = (By.CSS_SELECTOR, "#widget a[href]")

    path = "/index.php?route=product/product&product_id=43"
    main_browser_tab_handle = ''

    def open_product_page(self):
        self.browser.get(url=self.browser.url + self.path)
        self.main_browser_tab_handle = self.browser.current_window_handle

    def find_add_to_cart_button(self):
        self._verify_element_presence(self.ADD_TO_CART_BUTTON)

    def find_breadcrumb_item(self):
        self._verify_element_presence(self.BREADCRUMB_ITEM)

    def find_product_image_additional(self):
        self._verify_element_presence(self.PRODUCT_IMAGE_ADDITIONAL)

    def find_product_info_active_tab(self):
        self._verify_element_presence(self.PRODUCT_INFO_ACTIVE_TAB)

    def find_add_to_wishlist_button(self):
        self._verify_element_presence(self.ADD_TO_WISHLIST_BUTTON)

    def find_qty_field(self):
        self._verify_element_presence(self.QTY_FIELD)

    def switch_out_of_iframe(self):
        self._switch_out_of_iframe()

    def switch_to_main_browser_tab(self):
        self._switch_to_another_browser_tab(self.main_browser_tab_handle)

    def click_facebook_like(self, opened_page_title):
        stored_browser_tabs = self._get_browser_current_windows()
        self.browser.switch_to.frame(0)
        self._click_facebook_like_widget(self.FACEBOOK_FRAME)
        new_browser_tab = self._verify_new_window_is_open(stored_browser_tabs)
        self._switch_to_another_browser_tab(new_browser_tab)
        self._verify_page_title(opened_page_title)

    def click_twitter_tweet(self, opened_page_title):
        stored_browser_tabs = self._get_browser_current_windows()
        self.browser.switch_to.frame(1)
        self._verify_element_presence(self.TWITTER_FRAME).click()
        new_browser_tab = self._verify_new_window_is_open(stored_browser_tabs)
        self._switch_to_another_browser_tab(new_browser_tab)
        self._verify_page_title(opened_page_title)
