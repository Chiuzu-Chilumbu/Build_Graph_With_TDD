"""conftest file that holds all needed pytest fixtures"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.acceptance_tests.pages.stack_page import StackPage
from tests.acceptance_tests.pages.queue_page import QueuePage



@pytest.fixture(scope="module")
def driver():
	"""set up webdriver for chromme (Reusable for all tests)"""
	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	yield driver
	driver.quit()
	

@pytest.fixture(scope="module")
def stack_page(driver):
    """navigate to Stack page and return StackPage Object"""
    driver.get("http://127.0.0.1:5001/stack")
    return StackPage(driver)



@pytest.fixture(scope="module")
def queue_page(driver):
    """Navigate to Queue page and return QueuePage object"""
    driver.get("http://127.0.0.1:5001/queue")
    return QueuePage(driver)
