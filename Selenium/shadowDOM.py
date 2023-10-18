import os
from xml.etree.ElementTree import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyshadow.main import Shadow
    
chrome_options = Options()  
chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.implicitly_wait(10)
driver.get("http://watir.com/examples/shadow_dom.html")
driver.maximize_window()

# Get Shadow Elements
shadowRoot = driver.execute_script('return document.querySelector("#shadow_host").shadowRoot')
print(shadowRoot.find_element(By.CSS_SELECTOR,"#shadow_content>span").text)

# Get Nested Shadow Elements
nestedRoot = driver.execute_script('return document.querySelector("#shadow_host").shadowRoot.querySelector("#nested_shadow_host").shadowRoot')
print(nestedRoot.find_element(By.CSS_SELECTOR,"#nested_shadow_content>div").text)

driver.close()
