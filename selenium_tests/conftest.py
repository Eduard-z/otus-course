import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service_chrome
from selenium.webdriver.firefox.service import Service as Service_firefox
from selenium.webdriver.edge.service import Service as Service_edge


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("~/Documents/git repos/drivers"))


@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = Service_chrome(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = Service_firefox(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = Service_edge(executable_path=drivers + "/msedgedriver")
        driver = webdriver.Edge(service=service)
    elif browser == "yandex":
        service = Service_chrome(executable_path=drivers + "/yandexdriver")
        driver = webdriver.Chrome(service=service)
    else:
        raise Exception("Driver not supported")

    driver.maximize_window()
    request.addfinalizer(driver.quit)

    driver.get(url)
    driver.url = url
    return driver
