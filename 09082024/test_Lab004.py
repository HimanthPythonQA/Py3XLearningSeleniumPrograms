import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():

    chrome_options = Options()
    # if we want to start chrome with an extension we need to use below code
    #chrome_options.add_extension("extension path")
    chrome_options.add_argument("--page-load-strategy=eager")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    #time.sleep(6)