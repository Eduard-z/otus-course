from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page(browser):
    browser.get(url=browser.url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(driver=browser, timeout=2)
    # wait until catalogue is displayed
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-grid img")))

    browser.find_element(By.CSS_SELECTOR, ".list-group .active")
    browser.find_element(By.XPATH, "//label[text()='Sort By:']")
    browser.find_element(By.XPATH, "//button//span[text()='Add to Cart']")
    browser.find_element(By.XPATH, "//div/div[contains(text(), 'Showing')]")
    browser.find_element(By.XPATH, "//button/span[text()= 'Currency']/ancestor::button")
