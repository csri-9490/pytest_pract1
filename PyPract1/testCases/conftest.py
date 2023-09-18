import pytest
from selenium import webdriver


@pytest.fixture(params=[{'uname':'reddy.csri@gmail.com','pwd':'Shivaya1@'}])
def logins(request):
    return request.param

# @pytest.fixture
# def setup():
#     driver=webdriver.Chrome()
#     return driver
@pytest.fixture(scope="class")
def setup(request):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return  request.config.getoption("--browser")

##################pyTest HTML Report###############
#it is a hook for adding Environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'softwaretestingboard'
#     config._metadata['Module Name'] = 'smc module'
#     config._metadata['Tester'] ='Jason'

# it is hook for delete/modify Environment  info to html report

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("plugins",None)