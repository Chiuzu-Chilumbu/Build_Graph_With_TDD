from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StackPage:
    """page object model for stack UI"""

    def __init__(self, driver):
        self.driver = driver

    
    # Locators
    STATUS_MESSAGE = (By.ID, "status")
    CAPACITY_INPUT = (By.ID, "capacity")
    STACK_INPUT = (By.ID, "stack-input")
    INITIALIZE_BUTTON = (By.XPATH, "//button[contains(text(), initializeStack)]")
    PUSH_BUTTON = (By.XPATH, "//button[contains(text(), 'Push')]")
    POP_BUTTON = (By.XPATH, "//button[contains(text(), 'Pop')]")



    # Actions
    def set_stack_capacity(self, capacity):
        capacity_input = self.driver.find_element(*self.CAPACITY_INPUT)
        capacity_input.clear()
        capacity_input.send_keys(str(capacity))
        self.driver.find_element(*self.INITIALIZE_BUTTON).click()


    def get_status_message(self):
        return self.driver.find_element(*self.STATUS_MESSAGE).text
    
    def push_item(self, value):
        input_box = self.driver.find_element(*self.STACK_INPUT)
        input_box.clear()
        input_box.send_keys(str(value))
        self.driver.find_element(*self.PUSH_BUTTON).click()

        # ✅ WAIT UNTIL STACK UPDATES
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "stack-item"))
        )

    
    def pop_item(self):
        """Click the pop button and wait for the stack to update"""
        pop_button = self.driver.find_element(*self.POP_BUTTON)
        pop_button.click()

        # ✅ WAIT FOR THE STACK TO UPDATE
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(pop_button)  # Wait until the old button reference is stale
        )

    
    def is_pop_button_enabled(self):
        return self.driver.find_element(*self.POP_BUTTON).is_enabled()
    

    def is_push_button_enabled(self):
        return self.driver.find_element(*self.PUSH_BUTTON).is_enabled()

    

    def get_stack_items(self):
        """Returns the list of items currently in the stack visualization"""
        stack_items = self.driver.find_elements(By.CLASS_NAME, "stack-item")

        # ✅ Ensure we fetch fresh data from the DOM
        items = [item.text for item in stack_items]
        print(f"DEBUG: Stack items found: {items}")  # Debugging Output

        return items
