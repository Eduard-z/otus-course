from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page(browser):
    browser.get(url=browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(driver=browser, timeout=2)
    # wait until text is displayed in page title
    wait.until(EC.title_is("Register Account"))

    browser.find_element(By.CSS_SELECTOR, "aside > div.list-group")
    browser.find_element(By.CSS_SELECTOR, "fieldset#account")
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    browser.find_element(By.LINK_TEXT, "Privacy Policy")
    browser.find_element(By.CSS_SELECTOR, "[value='1'][name='newsletter']")
    browser.find_element(By.CSS_SELECTOR, "[value='Continue']")
