import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ["enable-logging"])
options.add_argument("--headless")

@pytest.fixture(params=['1', '2'], scope='module', autouse=False)
def show(request):
    print(f'start fixture for num {request.param}')
    yield f'fixture param = {request.param}'
    print('end fixture')

@pytest.fixture(scope='function')
def fun_browser(request):
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.close()

@pytest.fixture(scope='class')
def cls_browser(request):
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.close()

@pytest.fixture(scope='session')
def ssn_browser(request):
    driver = webdriver.Chrome(options=options)
    # request.cls.driver = driver
    yield driver
    driver.close()