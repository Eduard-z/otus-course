from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page(browser):
    browser.get(url=browser.url + "/admin")
    wait = WebDriverWait(driver=browser, timeout=2)
    # wait until login form is displayed
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "panel-default")))

    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
