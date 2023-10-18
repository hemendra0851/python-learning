import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()  
chrome_options.add_argument('--proxy-server=http://10.62.35.254')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_argument('--single-process')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument("--log-level=OFF")
s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("http://vkiosk-sdm-e.pharma-smart.net:9000")
# driver.maximize_window()
time.sleep(10)

# driver.close()
