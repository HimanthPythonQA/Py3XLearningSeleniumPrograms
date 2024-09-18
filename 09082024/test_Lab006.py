import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    driver.maximize_window()
    print(driver.page_source)
    time.sleep(20)
    driver.close() #// it closes only the present working tab
    #driver.quit()# it closes all the tabs


