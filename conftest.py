import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Фикстура для запуска браузера перед каждым тестом
    и его корректного закрытия после.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

stellarburgers.nomoreparties.site (https://stellarburgers.nomoreparties.site/)
Stellar Burgers
Web site created using create-react-app