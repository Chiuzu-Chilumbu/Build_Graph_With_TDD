from selenium.webdriver.common.by import By

class StackPage:
    """page object model for stack UI"""

    def __init__(self, driver):
        self.driver = driver

    
    # Locators
    STATUS_MESSAGE = (By.ID, "status")
    CAPACITY_INPUT = (By.ID, "capacity")
    INITIALIZE_BUTTON = (By.XPATH, "//button[contains(text(), initializeStack)]")



    # Actions
    def set_stack_capacity(self, capacity):
        capacity_input = self.driver.find_element(*self.CAPACITY_INPUT)
        capacity_input.clear()
        capacity_input.send_keys(str(capacity))
        self.driver.find_element(*self.INITIALIZE_BUTTON).click()


    def get_status_message(self):
        return self.driver.find_element(*self.STATUS_MESSAGE).text