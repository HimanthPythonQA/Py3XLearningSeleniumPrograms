import time
import openpyxl
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
from selenium.webdriver.common.alert import Alert
import os

class TestAlerts:

    @pytest.mark.qa
    def test_alerts_tc1(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        element_prompt = self.driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
        element_prompt.click()
        # for alert to come we will add a wait
        wait = WebDriverWait(driver=self.driver,timeout=3)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID,"result").text
        assert result == "You successfully clicked an alert"

    def test_alerts_tc2_confirm_alert(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        element_prompt = self.driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
        element_prompt.click()
        # for alert to come we will add a wait
        wait = WebDriverWait(driver=self.driver, timeout=3)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        assert result == "You clicked: Ok"

    def test_alerts_tc3_confirm_alert_text(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        element_prompt = self.driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
        element_prompt.click()
        # for alert to come we will add a wait
        wait = WebDriverWait(driver=self.driver, timeout=3)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        alert.send_keys("himanth")
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        assert result == "You entered: himanth"

    def test_checkbox(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        self.driver.maximize_window()
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkboxes[0].click()
        time.sleep(6)

