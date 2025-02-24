from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QueuePage:
    """Page object model for the Queue UI"""

    def __init__(self, driver):
        self.driver = driver 

    
    # Locators
    STATUS_MESSAGE = (By.ID, "status")
    CAPACITY_INPUT = (By.ID, "capacity")
    INITIALISE_BUTTON = (By.XPATH, "//button[contains(text(), 'Initialize Queue')]")


    # Actions
    def set_queue_capacity(self, capacity):
        """Set queue capacity and initialise"""
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.CAPACITY_INPUT)
        )

        capacity_input = self.driver.find_element(*self.CAPACITY_INPUT)
        capacity_input.clear()
        capacity_input.send_keys(str(capacity))
        self.driver.find_element(*self.INITIALISE_BUTTON).click()


    def get_status_message(self):
        """Retives the status message displayed on the UI"""
        return self.driver.find_element(By.ID, "status").text