from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-fullscreen")

driver = webdriver.Chrome(options=options)
url = "https://fundingsocieties.com"
driver.get(url)


### Get total approved loans of each Q ###
driver.find_element(By.XPATH,"//div[contains(@role,'navigation')]//a[contains(@class,'t-l-base-gray-darker')][normalize-space()='Statistics']").click()
sleep(3)
print("Get total approved loans of each Q")
markers = driver.find_elements(By.XPATH,"//*[local-name()='g'][contains(@class,'highcharts-markers')]/*[local-name()='path']")
for m in markers:
    m.click()
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[local-name()='g'][contains(@class,'highcharts-label')]/*[local-name()='text']"))
        )
        tspans = element.find_elements(By.XPATH, "./*[local-name()='tspan']")
        if len(tspans) > 3:
            print("%s = %s" % (tspans[0].text, tspans[3].text))
    except TimeoutException:
        pass

### Get total amount disbursed each Q ###
print("Get total amount disbursed each Q")

driver.find_element(By.XPATH,"//label[normalize-space()='Amount disbursed']").click()
sleep(3)
print("Get total approved loans of each Q")
markers = driver.find_elements(By.XPATH,"//*[local-name()='g'][contains(@class,'highcharts-markers')]/*[local-name()='path']")
for m in markers:
    m.click()
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[local-name()='g'][contains(@class,'highcharts-label')]/*[local-name()='text']"))
        )
        tspans = element.find_elements(By.XPATH, "./*[local-name()='tspan']")
        if len(tspans) > 3:
            print("%s = %s" % (tspans[0].text, tspans[3].text))
    except TimeoutException:
        pass

### Get total default rate each Q ###
print("Get default rate each Q")

driver.find_element(By.XPATH,"//label[normalize-space()='Default rate']").click()
sleep(3)
print("Get total approved loans of each Q")
markers = driver.find_elements(By.XPATH,"//*[local-name()='g'][contains(@class,'highcharts-markers')]/*[local-name()='path']")
for m in markers:
    m.click()
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[local-name()='g'][contains(@class,'highcharts-label')]/*[local-name()='text']"))
        )
        tspans = element.find_elements(By.XPATH, "./*[local-name()='tspan']")
        if len(tspans) > 3:
            print("%s = %s" % (tspans[0].text, tspans[3].text))
    except TimeoutException:
        pass
