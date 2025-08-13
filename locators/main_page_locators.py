from selenium.webdriver.common.by import By

class MainPageLocators:
    USER_AVATAR = (By.CSS_SELECTOR, ".user-avatar")
    USER_NAME = (By.XPATH, "//span[contains(@class,'user-name')]")
    PLACE_AD_BTN = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    LOGIN_REGISTER_BTN = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    LOGOUT_BTN = (By.XPATH, "//button[contains(text(),'Выйти')]")
