import pytest
from selenium import webdriver

from Utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    if browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    if browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser option from chrome/firefox/edge.")
    app_url = ReadConfigurations.read_configurations("basic info","url")
    driver.get(app_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()