import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sprint_5.locators import HOME_URL, BUTTON_LOGIN, LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT
from Sprint_5.conftest import register_user

def login_via_login_form(driver, email, password):
    driver.get(HOME_URL + "login")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL)).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*LOGIN_SUBMIT).click()
    time.sleep(1)

def test_login_from_main_button(driver, new_user):
    # сначала регистрируем
    register_user(driver, new_user["name"], new_user["email"], new_user["password"])
    # теперь логин через главную кнопку "Войти в аккаунт"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()
    login_via_login_form(driver, new_user["email"], new_user["password"])
    assert "account" in driver.current_url or len(driver.find_elements_by_xpath("//h2[contains(text(),'Личный кабинет')]")) > 0