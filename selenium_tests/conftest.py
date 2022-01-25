import pytest
import os
import logging
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service_chrome
from selenium.webdriver.firefox.service import Service as Service_firefox
from selenium.webdriver.edge.service import Service as Service_edge


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--environment", action="store", default="local")
    parser.addoption("--executor", action="store", default="192.168.100.144:4444")
    parser.addoption("--browser_version", action="store", default="96.0")
    parser.addoption("--drivers", action="store",
                     default=os.path.expanduser("~/Documents/git repos/drivers"))
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    environment = request.config.getoption("--environment")
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--browser_version")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('driver')
    test_name = request.node.name
    logger.setLevel(level=log_level)

    log_file = logging.FileHandler(f"selenium_tests/logs/{test_name}.log", mode="a")
    format_logs = logging.Formatter("%(levelname)s %(name)s: %(filename)s:%(lineno)d %(message)s")
    log_file.setFormatter(format_logs)
    logger.addHandler(log_file)

    logger.info(f"===> Test '{test_name}' started at {datetime.datetime.now()}")

    if environment == "local":
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

    elif environment == "selenoid":
        executor_url = f"http://{executor}/wd/hub"

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.browser_version = browser_version
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.browser_version = browser_version
        elif browser == "MicrosoftEdge":
            options = webdriver.EdgeOptions()
            options.browser_version = browser_version
        else:
            raise Exception("Browser not supported")

        driver = webdriver.Remote(command_executor=executor_url, options=options)

    else:
        raise Exception("Environment not supported")

    logger.info(f"Browser: {browser, driver.capabilities}")

    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info(f"===> Test '{test_name}' finished at {datetime.datetime.now()}")

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url
    driver.log_level = log_level
    driver.test_name = test_name

    return driver
