from selenium.webdriver.common.by import By

class AdPageLocators:
    TITLE_INPUT = (By.NAME, "title")
    DESCRIPTION_INPUT = (By.NAME, "description")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    CONDITION_NEW = (By.XPATH, "//input[@type='radio' and @value='new']")
    PUBLISH_BTN = (By.XPATH, "//button[contains(text(),'Опубликовать')]")
    MY_ADS_SECTION = (By.XPATH, "//div[@class='my-ads']")