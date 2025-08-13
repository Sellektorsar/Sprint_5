from data import urls, test_data
from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators
from utils.helpers import generate_email, wait_for_element

class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(urls.BASE_URL)
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_data.NEW_USER_PASSWORD)
        driver.find_element(*AuthPageLocators.PASSWORD_REPEAT_INPUT).send_keys(test_data.NEW_USER_PASSWORD)
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BTN).click()

        wait_for_element(driver, MainPageLocators.USER_AVATAR)
        username = wait_for_element(driver, MainPageLocators.USER_NAME).text
        assert username == "User"

    def test_registration_invalid_email(self, driver):
        driver.get(urls.BASE_URL)
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys("invalid_email")
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BTN).click()

        assert wait_for_element(driver, AuthPageLocators.ERROR_MESSAGE).is_displayed()

    def test_registration_existing_user(self, driver):
        driver.get(urls.BASE_URL)
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(test_data.TEST_USER_EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_data.TEST_USER_PASSWORD)
        driver.find_element(*AuthPageLocators.PASSWORD_REPEAT_INPUT).send_keys(test_data.TEST_USER_PASSWORD)
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BTN).click()

        assert wait_for_element(driver, AuthPageLocators.ERROR_MESSAGE).is_displayed()