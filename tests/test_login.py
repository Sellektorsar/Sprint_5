from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators
from utils.helpers import wait_for_element, generate_email

class TestLogin:

    def test_login_success(self, driver):
        email = generate_email()
        password = "Qwerty123!"

        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.PASSWORD_REPEAT_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BTN).click()

        driver.find_element(*MainPageLocators.LOGOUT_BTN).click()
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_BTN).click()

        username = wait_for_element(driver, MainPageLocators.USER_NAME).text
        assert username == "User"