import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Sprint_5.locators import HOME_URL, BUTTON_LOGIN, REG_NAME, REG_EMAIL, REG_PASSWORD, REG_SUBMIT, LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_SUBMIT, BUTTON_PROFILE

# Параметринг браузера
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        drv = webdriver.Chrome()
    elif browser == "firefox":
        drv = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    drv.maximize_window()
    yield drv
    drv.quit()

# Утилиты для тестов
def generate_unique_email(first="veronika", last="akhmetzyanova", cohort=30, domain="yandex.ru"):
    """ Возвращает email в формате: firstname_lastname_cohort_XXX@domain """
    rand3 = random.randint(100, 999)
    return f"{first}_{last}_{cohort}_{rand3}@{domain}"

def generate_password(min_len=6):
    # простой генератор пароля >= 6 символов
    s = "Pwd" + str(int(time.time()))[-6:]
    return s
# Фикстура для регистрации нового пользователя
@pytest.fixture
def register_user(driver):
    """Фикстура для регистрации нового пользователя"""
    driver.get(HOME_URL)
    driver.find_element(By.XPATH, "//a[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

    driver.find_element(By.XPATH, REG_NAME).send_keys("Veronika")
    driver.find_element(By.XPATH, REG_EMAIL).send_keys("veronika_akhmetzyanova_30_331@yandex.ru")
    driver.find_element(By.XPATH, REG_PASSWORD).send_keys("123456")
    driver.find_element(By.XPATH, REG_SUBMIT).click()

    return driver

@pytest.fixture
def new_user():
    email = generate_unique_email()
    password = generate_password()
    name = "Veronika"
    return {"email": email, "password": password, "name": name}

# Функция регистрации (внутренняя, не фикстура)
def register_user(driver, name, email, password):
    driver.get(HOME_URL)
    # перейти в форму регистрации: можно нажать "Войти в аккаунт" -> затем "Зарегистрироваться"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    driver.get(HOME_URL + "register")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(REG_NAME)).send_keys(name)
    driver.find_element(*REG_EMAIL).send_keys(email)
    driver.find_element(*REG_PASSWORD).send_keys(password)
    driver.find_element(*REG_SUBMIT).click()
    time.sleep(1)