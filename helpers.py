from selenium.webdriver.common.by import By
from locators import REG_NAME, REG_EMAIL, REG_PASSWORD, REG_SUBMIT, BUTTON_LOGIN, HOME_URL

def register_user(driver, name, email, password):
    """
    Регистрирует нового пользователя на сайте Stellar Burgers.
    """
    driver.get(HOME_URL)
    driver.find_element(*BUTTON_LOGIN).click()
    driver.find_element(*REG_NAME).send_keys(name)
    driver.find_element(*REG_EMAIL).send_keys(email)
    driver.find_element(*REG_PASSWORD).send_keys(password)
    driver.find_element(*REG_SUBMIT).click()