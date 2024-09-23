import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.chrome.options import Options


@pytest.mark.positive
@allure.title("open the sign up URL of vwo.com-test_mini_project_3")
@allure.description("verify that clicking on button Start a free trial, url changes")
def test_mini_project_3():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT,"Start a")
    anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(4)
    driver.quit()