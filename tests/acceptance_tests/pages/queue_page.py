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
    QUEUE_INPUT = (By.ID, "queue-input")
    INITIALISE_BUTTON = (By.XPATH, "//button[contains(text(), 'Initialize Queue')]")
    ENQUEUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Enqueue')]")
    DEQUEUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Dequeue')]")
    QUEUE_ITEMS = (By.CLASS_NAME, "queue-item")


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
    

    def enqueue_item(self, value):
        """Enqueue an item into the queue"""
        input_box = self.driver.find_element(*self.QUEUE_INPUT)
        input_box.clear()
        input_box.send_keys(str(value))
        self.driver.find_element(*self.ENQUEUE_BUTTON).click()

        # Wait unti queue updates
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.QUEUE_ITEMS)
        )


    def dequeue_item(self):
        """Dequeue an item form the queue"""
        dequeue_button = self.driver.find_element(*self.DEQUEUE_BUTTON)
        dequeue_button.click()

        # Wait for queue to update
        WebDriverWait(self.driver, 5).until(
            EC.staleness_of(dequeue_button) # wait until the old button reference is stale
        )


    def is_dequeue_button_enabled(self):
        """Check if dequeue button is enabled"""
        return self.driver.find_element(*self.DEQUEUE_BUTTON).is_enabled()



    def get_queue_items(self):
        """Returns the list of items currently in the queue visualization"""
        queue_items = self.driver.find_elements(*self.QUEUE_ITEMS)

        # Ensure we fetch fresh data from the DOM
        items = [item.text for item in queue_items]
        return items