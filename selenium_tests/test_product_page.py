from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page(browser):
    browser.get(url=browser.url + "/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver=browser, timeout=2)
    # wait until button is displayed
    wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "input[name='product_id'] ~ button")
    ))

    browser.find_element(By.CSS_SELECTOR, ".breadcrumb a")
    browser.find_element(By.CSS_SELECTOR, ".image-additional")
    browser.find_element(By.CSS_SELECTOR, ".active > a")
    browser.find_element(By.CSS_SELECTOR,
                         ".btn-group > button[data-original-title='Add to Wish List']")
    browser.find_element(By.CSS_SELECTOR, "[name='quantity']")
