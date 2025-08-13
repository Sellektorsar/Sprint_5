from selenium.webdriver.common.by import By

class AuthPageLocators:
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_REPEAT_INPUT = (By.NAME, "repeatPassword")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")
    LOGIN_BTN = (By.XPATH, "//button[contains(., 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(text(),'Ошибка')]")