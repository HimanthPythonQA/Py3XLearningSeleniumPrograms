import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    driver = webdriver.Chrome()

    # Create an instance of Chromeoptions
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920*1080")
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")

    time.sleep(10)
