import time
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Sprint_5.locators import HOME_URL, TAB_BUNS, TAB_SAUCES, TAB_FILLINGS

def test_constructor_tabs_visible(driver):
    driver.get(HOME_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TAB_BUNS))
    assert driver.find_element(*TAB_BUNS).is_displayed()
    assert driver.find_element(*TAB_SAUCES).is_displayed()
    assert driver.find_element(*TAB_FILLINGS).is_displayed()