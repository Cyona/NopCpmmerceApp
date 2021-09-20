from selenium import webdriver
import pytest


def pytest_addoption(parser):  #get value from CLi,hook
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="G:\\Cyona\\Udemy\\python\\Driver\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="G:\\Cyona\\Udemy\\python\\Driver\\edgedriver_win64\\msedgedriver.exe")

    return driver


#######pytest html report##########

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Cyona'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
