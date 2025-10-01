
import time
import pytest

from selenium.webdriver.common.by import By
from Sprint_5.locators import HOME_URL, REG_NAME, REG_EMAIL, REG_PASSWORD, REG_SUBMIT

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(HOME_URL)

        driver.find_element(By.XPATH, "//a[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        driver.find_element(By.XPATH, REG_NAME).send_keys("Veronika")
        driver.find_element(By.XPATH, REG_EMAIL).send_keys("veronika_akhmetzyanova_30_331@yandex.ru")
        driver.find_element(By.XPATH, REG_PASSWORD).send_keys("StrongPass123")
        driver.find_element(By.XPATH, REG_SUBMIT).click()

        assert driver.find_element(By.XPATH, "//h2[text()='Вход']")

    def test_registration_with_short_password(self, driver):
        driver.get(HOME_URL)

        driver.find_element(By.XPATH, "//a[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        driver.find_element(By.XPATH, REG_NAME).send_keys("Veronika")
        driver.find_element(By.XPATH, REG_EMAIL).send_keys("wrong_pass_test_331@yandex.ru")
        driver.find_element(By.XPATH, REG_PASSWORD).send_keys("123")  # слишком короткий
        driver.find_element(By.XPATH, REG_SUBMIT).click()

        # Проверка текста ошибки
        error = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text
        assert error == "Некорректный пароль"