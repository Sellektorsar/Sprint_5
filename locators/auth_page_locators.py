from selenium.webdriver.common.by import By

class AuthPageLocators:
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_REPEAT_INPUT = (By.NAME, "confirmPassword")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(),'Ошибка')]")