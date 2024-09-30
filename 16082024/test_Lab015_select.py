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
@pytest.mark.positive
def test_katalon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    element_select = driver.find_element(By.ID,"dropdown")
    select = Select(element_select)
    select.select_by_visible_text("Option 1")

    time.sleep(10)