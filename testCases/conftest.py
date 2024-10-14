import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run the tests")

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser: {}".format(browser))

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# html reports using pytest-html and metadata
import pytest

def pytest_configure(config):
    # Ensure that metadata is available
    if hasattr(config, 'metadata'):
        config.metadata['Project Name'] = 'codefios'
        config.metadata['Module Name'] = 'tests'
        config.metadata['Tester'] = 'Nabil'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # Remove unnecessary metadata entries
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

    # Add custom metadata entries if necessary
    metadata['Project Name'] = 'codefios'
    metadata['Module Name'] = 'tests'
    metadata['Tester'] = 'Nabil'


