from selenium.webdriver.common.by import By

class ModalLocators:
    AUTH_REQUIRED_TITLE = (By.XPATH, "//h2[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]")