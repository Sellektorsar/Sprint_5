from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()

def generate_email():
    return fake.email()

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))