from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-notifications')
options.add_argument("--guest")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Edge(options=options)
driver.get('https://demo.automationtesting.in/Alerts.html')
driver.maximize_window()
driver.implicitly_wait(10)

assert driver.title == 'Alerts'

################ Alert with OK ####################################3

driver.find_element(By.ID, 'OKTab').click()
sleep(1)
driver.switch_to.alert.accept()

################ Alert with OK ad Cancel ###########################

driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()
sleep(1)

driver.find_element(By.XPATH, "//div[@id='CancelTab']//button").click()
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
assert driver.find_element(By.ID, 'demo').text == 'You pressed Ok'

driver.find_element(By.XPATH, "//div[@id='CancelTab']//button").click()
sleep(1)
driver.switch_to.alert.dismiss()
sleep(1)
assert driver.find_element(By.ID, 'demo').text == 'You Pressed Cancel'

############### Alert with Textbox ################################

driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
sleep(1)

driver.find_element(By.XPATH, "//div[@id='Textbox']//button").click()
sleep(1)
obj = driver.switch_to.alert
sleep(1)
obj.send_keys('Test')
sleep(1)
obj.accept()
sleep(1)
assert driver.find_element(By.ID, 'demo1').text == 'Hello Test How are you today'

driver.find_element(By.XPATH, "//div[@id='Textbox']//button").click()
sleep(1)
driver.switch_to.alert.dismiss()
sleep(1)
assert driver.find_element(By.ID, 'demo1').text == ''

driver.quit()