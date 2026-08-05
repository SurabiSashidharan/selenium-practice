from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "https://the-internet.herokuapp.com/login"
    username_input=(By.ID, "username")
    password_input=(By.ID, "password")
    button_login=(By.CLASS_NAME, "radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.button_login).click()

    def get_flash_text(self):
        raw = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FLASH_MESSAGE)).text
        return raw.replace('×', "").strip()