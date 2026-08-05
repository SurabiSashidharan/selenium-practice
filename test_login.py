import pytest
import json
from selenium import webdriver
from pages.login_page import LoginPage
from pathlib import Path
import pandas as pd



# def test_successful_login(driver):
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login("tomsmith", "SuperSecretPassword!")
#     text=login_page.get_flash_text()
#     assert "You logged into a secure area!" in text

# def test_wrong_password_shows_correct_error(driver):
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login("tomsmith", "WrongPassword!")
#     text=login_page.get_flash_text()
#     assert "Your password is invalid!" in text


#-------------------------------------------------------------------------------------------------

#parameterized test for login functionality

# @pytest.mark.parametrize("username,password,expected_message", [
#     ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
#     ("tomsmith", "WrongPassword!", "Your password is invalid!"),("WrongUsername","SuperSecretPassword!","Your username is invalid!")
# ])

# def test_login(driver, username, password, expected_message):
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login(username, password)
#     assert expected_message in login_page.get_flash_text()

#--------------------------------------------------------------------------------------------------------------------------
#Data driven testing using external data source (CSV, JSON, Excel, etc.) can be implemented by reading the data from 

def load_login_data_json():
    data_path = Path(__file__).parent / "test_data" / "login_data.json"
    with open(data_path) as f:
        return json.load(f)

def load_login_data_excel():
    data_path = Path(__file__).parent / "test_data" / "login_data.xlsx"
    df = pd.read_excel(data_path)
    return df.to_dict("records")

# @pytest.mark.parametrize("case", load_login_data_excel())
# def test_login(driver, case):
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login(case["username"], case["password"])
#     assert case["expected_message"] in login_page.get_flash_text()

@pytest.mark.parametrize("case", load_login_data_json(), ids=lambda case: case["scenario"])
def test_login(driver, case):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(case["username"], case["password"])
    assert case["expected_message"] in login_page.get_flash_text()


