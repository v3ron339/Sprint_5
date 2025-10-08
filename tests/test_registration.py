# tests/test_constructor.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Sprint_5.locators import (
    HOME_URL,
    BUTTON_CONSTRUCTOR,
    TAB_BUNS, TAB_SAUCES, TAB_FILLINGS,
    SECTION_BUNS, SECTION_SAUCES, SECTION_FILLINGS,
    INGREDIENT_ITEM
)


class TestConstructor:
    @pytest.mark.parametrize(
        "tab_locator, section_locator, name",
        [
            (TAB_BUNS, SECTION_BUNS, "Булки"),
            (TAB_SAUCES, SECTION_SAUCES, "Соусы"),
            (TAB_FILLINGS, SECTION_FILLINGS, "Начинки"),
        ]
    )
    def test_constructor_tabs_navigation(self, driver, tab_locator, section_locator, name):
        
        wait = WebDriverWait(driver, 10)

        # Открываем главную и переходим в конструктор
        driver.get(HOME_URL)
        wait.until(EC.element_to_be_clickable(BUTTON_CONSTRUCTOR)).click()

        # Убедиться, что конструктор загрузился (ждём видимости первой вкладки)
        wait.until(EC.visibility_of_element_located(TAB_BUNS))

        # Кликаем по проверяемой вкладке
        tab = wait.until(EC.element_to_be_clickable(tab_locator))
        tab.click()

        # Попытка: ждём появления уникального блока секции
        section_visible = False
        try:
            wait.until(EC.visibility_of_element_located(section_locator))
            section_visible = True
        except TimeoutException:
            # Если уникальная секция не появилась — проверяем активный класс у вкладки
            # Ждём, пока вкладка получит "активный" класс (варианты названия класса могут отличаться)
            def tab_is_active(drv):
                cls = tab.get_attribute("class") or ""
                cls = cls.lower()
                return ("active" in cls) or ("current" in cls) or ("tab_tab_type_current" in cls)

            try:
                wait.until(tab_is_active)
                section_visible = True
            except TimeoutException:
                section_visible = False

        assert section_visible, f"Переход на вкладку {name} не сработал (нет секции и вкладка не активна)"

        # Дополнительная проверка: в секции есть хотя бы один элемент ингредиента (если селектор задан)
        items = driver.find_elements(*INGREDIENT_ITEM)
        assert len(items) > 0, f"Вкладка {name}: список ингредиентов пуст после перехода"