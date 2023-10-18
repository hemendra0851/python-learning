import os
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

shadowHost = driver.find_element(By.XPATH, "//div[@id='shadow_host']")
ele = driver.execute_script("return arguments[0].shadowRoot", shadowHost)
print(ele)
# shadow = Shadow(driver)
# shadowHost = shadow.find_element(By.XPATH, "//div[@id='shadow_host']")

root = driver.execute_script('return document.querySelector("#shadow_host").shadowRoot.querySelector("#shadow_content")')
print(root)
print(root.find_element(By.CSS_SELECTOR,".info").text)

driver.close()
