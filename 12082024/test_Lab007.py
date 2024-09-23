import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options


@pytest.mark.positive
@allure.title("verify that url changes when we click on make appointment button")
@allure.description("verify the url changes")
def test_mini_project_1():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # we need to find the unique attribute which can find the element
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")

    # click on it
    make_appointment_element.click()

    # verify that url changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()