from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(url=browser.url)
    wait = WebDriverWait(driver=browser, timeout=2)
    # wait until navigation bar is displayed
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-collapse")))

    browser.find_element(By.CSS_SELECTOR, "a[title='My Account'] span.hidden-xs")
    browser.find_element(By.NAME, "search")
    browser.find_element(By.CSS_SELECTOR, ".btn-inverse")
    browser.find_element(By.LINK_TEXT, "Your Store")
    browser.find_element(By.CSS_SELECTOR, ".product-layout")
