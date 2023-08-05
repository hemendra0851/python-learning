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
driver.get('https://demo.automationtesting.in/Windows.html')
driver.maximize_window()
driver.implicitly_wait(10)

assert driver.title == 'Frames & windows'

parentWin = driver.current_window_handle

def newTab():

    driver.find_element(By.XPATH, "//button[text()='    click   ']").click()
    sleep(2)
    # Switched by default to new tab
    allWindows = driver.window_handles

    driver.switch_to.window(parentWin)
    sleep(1)
    driver.switch_to.window(allWindows[-1])
    sleep(1)
    driver.switch_to.window(parentWin)
    sleep(1)

def newWin():

    driver.find_element(By.XPATH, "//a[@href='#Seperate']").click()
    sleep(1)

    driver.find_element(By.XPATH, "//div[@id='Seperate']//button").click()
    sleep(2)
    # Switched by default to new tab
    allWindows = driver.window_handles

    driver.switch_to.window(parentWin)
    sleep(1)
    driver.switch_to.window(allWindows[-1])
    sleep(1)
    driver.close()

def multiWin():

    driver.find_element(By.XPATH, "//a[@href='#Multiple']").click()
    sleep(1)

    driver.find_element(By.XPATH, "//div[@id='Multiple']//button").click()
    sleep(2)
    # Switched by default to new tab
    allWindows = driver.window_handles

    driver.switch_to.window(parentWin)
    sleep(1)
    driver.switch_to.window(allWindows[-1])
    sleep(1)
    driver.close()

multiWin()
driver.quit()