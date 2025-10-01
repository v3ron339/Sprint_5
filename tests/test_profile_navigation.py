import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import HOME_URL, BUTTON_PROFILE, LOGO, TAB_BUNS
from Sprint_5.conftest import register_user

def test_profile_and_constructor_and_logo(driver, new_user):
    # регистрация и переход в профиль
    register_user(driver, new_user["name"], new_user["email"], new_user["password"])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_PROFILE)).click()
    assert "account" in driver.current_url

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGO)).click()
    # проверяем наличие вкладки Булки/Начинки
    assert len(driver.find_elements(*TAB_BUNS)) > 0