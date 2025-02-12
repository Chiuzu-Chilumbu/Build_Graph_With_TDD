"""conftest file that holds all needed pytest fixtures"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app.models.queue_adt import Queue
from app.models.stack_adt import Stack
from app.models.graph_adt import Graph



@pytest.fixture(scope='function')
def new_queue():
	"""fixture to provide a new queue for each test"""
	return Queue(5)


@pytest.fixture(scope='function')
def new_stack():
	"""fixture to provide a new queue for each test"""
	return Stack(5)


@pytest.fixture(scope='function')
def new_graph():
	"""ficture to provde a new graph for each test"""
	return Graph()



@pytest.fixture(scope="module")
def driver():
	"""set up webdriver for chromme (Reusable for all tests)"""
	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	yield driver
	driver.quit()