from selenium.webdriver.common.by import By

# --- Главная страница ---
HOME_URL = "https://stellarburgers.nomoreparties.site/"

# --- Кнопки входа/выхода ---
BUTTON_LOGIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
BUTTON_PROFILE = (By.XPATH, "//a[contains(@href,'/account')]")
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")

# --- Регистрация ---
REG_NAME = (By.NAME, "name")
REG_EMAIL = (By.NAME, "email")
REG_PASSWORD = (By.NAME, "password")
REG_SUBMIT = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
REG_TO_LOGIN = (By.XPATH, "//a[contains(text(),'Войти')]")

# --- Авторизация (форма входа) ---
LOGIN_EMAIL = (By.NAME, "email")
LOGIN_PASSWORD = (By.NAME, "password")
LOGIN_SUBMIT = (By.XPATH, "//button[contains(text(),'Войти')]")

# --- Личный кабинет ---
PROFILE_HEADER = (By.XPATH, "//h2[contains(text(),'Личный кабинет')]")

# --- Навигация (Конструктор) ---
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
LOGO = (By.CSS_SELECTOR, "a[aria-label='Stellar Burgers']")

# --- Вкладки конструктора ---
TAB_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")
TAB_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")
TAB_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]")