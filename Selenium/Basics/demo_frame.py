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
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
# driver.implicitly_wait(10)

assert driver.title == 'Frames'

def singleFrame():

    try:
        driver.find_element(By.TAG_NAME, "input").send_keys("Hello")
    except Exception:
        print('Element not visible outside iframe')
    finally:
        driver.switch_to.frame(frame_reference='singleframe')
        driver.find_elements(By.TAG_NAME, "input")[0].send_keys("Hello")
        driver.switch_to.default_content()

def nestedFrame():

    driver.find_element(By.XPATH, "//a[@href='#Multiple']").click()
    sleep(1)

    driver.switch_to.frame(frame_reference=driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']"))
    driver.switch_to.frame(frame_reference=driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']"))
    driver.find_elements(By.TAG_NAME, "input")[0].send_keys("Hello")

nestedFrame()
driver.quit()