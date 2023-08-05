'''
Setup:

pip install webdriver-manager

'''
# from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from time import sleep
import unittest

# Chrome Libraries
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.chrome.service import Service as chrome_Service
from webdriver_manager.chrome import ChromeDriverManager

# Edge Libraries
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as edge_Options
from selenium.webdriver.edge.service import Service as edge_Service


def set_chromeOptions():
    chrome_options = chrome_Options()  
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.headless = True
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument('--single-process')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--remote-debugging-port=9222")
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument("--log-level=OFF")
    return chrome_options

def set_edgeOptions():
    edge_options = edge_Options()
    edge_options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    edge_options.add_argument('--disable-dev-shm-usage')
    edge_options.add_argument('--log-level=OFF')
    return edge_options

def set_chromeDriverManager():
    ChromeDriverManager(path = r".\\Drivers").install()

    return chrome_Service(ChromeDriverManager().install())

def set_edgeDriverManager():
    return edge_Service(EdgeChromiumDriverManager().install())

def create_webdriver(browser, service, options):

    driver = webdriver.Chrome(service=service, options=options) if browser == 'chrome' else webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


# chrome_options = set_chromeOptions()
# service= set_chromeDriverManager()

edge_options = set_edgeOptions()
service = set_edgeDriverManager()

driver = create_webdriver('edge', service, edge_options)

url= 'http://tutorialsninja.com/demo/index.php'

driver.get(url)
driver.maximize_window()

sleep(1)

cart= driver.find_element(By.XPATH, "//span[@id='cart-total']")

products= driver.find_elements(By.XPATH, "//*[contains(@class,'product-layout')]//h4/a")
for product in products:
    product_name = product.text
    print('Product= ' + product_name)
    
print(cart.text)

addToCart= driver.find_elements(By.XPATH, "//span[text()= 'Add to Cart']")
addToCart[0].click()
addToCart[1].click()

sleep(1)
print(cart.text)
cart.click()





driver.quit()