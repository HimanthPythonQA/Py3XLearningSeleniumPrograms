import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    try:
       textarea = driver.find_element(By.NAME,"q")
       driver.refresh()
       textarea = driver.find_element(By.NAME,"q")
       textarea.send_keys("the testing academy")
    except StaleElementReferenceException as see:
        print(see)

    time.sleep(6)
    driver.close()