import pytest
from tests.acceptance_tests.pages.queue_page import QueuePage
from selenium.webdriver.support.ui import WebDriverWait

pytestmark = pytest.mark.queue_acceptance_test

@pytest.fixture(scope="module")
def queue_page(driver):
    """Navigate to Queue page and return QueuePage object"""
    driver.get("http://127.0.0.1:5001/queue")
    return QueuePage(driver)



def test_initialise_queue(queue_page):
    """Test Queue Initialization"""
    queue_page.set_queue_capacity(5)
    assert "Queue initialized successfully!" in queue_page.get_status_message()