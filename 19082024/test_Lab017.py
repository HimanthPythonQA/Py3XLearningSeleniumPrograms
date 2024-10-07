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


@pytest.mark.positive
def test_svgelements():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)
    states = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in states:
        print(state.get_attribute("aria-label"))

        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(10)
    allure.attach(driver.get_screenshot_as_png(), name="svg_elements", attachment_type=AttachmentType.PNG)
    driver.quit()
