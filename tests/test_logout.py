from data import urls, test_data
from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators
from utils.helpers import wait_for_element

class TestLogout:

    def test_logout_success(self, driver):
        driver.get(urls.BASE_URL)
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(test_data.TEST_USER_EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_data.TEST_USER_PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_BTN).click()

        wait_for_element(driver, MainPageLocators.USER_NAME)
        driver.find_element(*MainPageLocators.LOGOUT_BTN).click()

        assert driver.find_element(*MainPageLocators.LOGIN_REGISTER_BTN).is_displayed()