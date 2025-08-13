from data import urls, test_data
from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators
from locators.ad_page_locators import AdPageLocators
from locators.modal_locators import ModalLocators
from utils.helpers import wait_for_element

class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        driver.get(urls.BASE_URL)
        driver.find_element(*MainPageLocators.PLACE_AD_BTN).click()
        modal_title = wait_for_element(driver, ModalLocators.AUTH_REQUIRED_TITLE)
        assert modal_title.is_displayed()

    def test_create_ad_authorized(self, driver):
        driver.get(urls.BASE_URL)
        driver.find_element(*AuthPageLocators.LOGIN_REGISTER_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(test_data.TEST_USER_EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_data.TEST_USER_PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_BTN).click()

        wait_for_element(driver, MainPageLocators.USER_NAME)
        driver.find_element(*MainPageLocators.PLACE_AD_BTN).click()

        driver.find_element(*AdPageLocators.TITLE_INPUT).send_keys("Тестовый товар")
        driver.find_element(*AdPageLocators.DESCRIPTION_INPUT).send_keys("Описание тестового товара")
        driver.find_element(*AdPageLocators.PRICE_INPUT).send_keys("1000")
        driver.find_element(*AdPageLocators.CATEGORY_DROPDOWN).send_keys("Электроника")
        driver.find_element(*AdPageLocators.CITY_DROPDOWN).send_keys("Москва")
        driver.find_element(*AdPageLocators.CONDITION_NEW).click()
        driver.find_element(*AdPageLocators.PUBLISH_BTN).click()

        my_ads = wait_for_element(driver, AdPageLocators.MY_ADS_SECTION)
        assert "Тестовый товар" in my_ads.text