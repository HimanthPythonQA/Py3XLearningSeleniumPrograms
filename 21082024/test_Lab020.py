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

def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    try:
         driver.find_element(By.NAME,"hima").send_keys("the testing academy")
    except NoSuchElementException as nse :
        print(f" No such element found, check locator {nse}")

    time.sleep(6)
    driver.close()