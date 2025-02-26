"""conftest file that holds all needed pytest fixtures"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.acceptance_tests.pages.stack_page import StackPage
from tests.acceptance_tests.pages.queue_page import QueuePage
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



@pytest.fixture
def sample_graph():
    """Fixture to create a sample graph for traversal tests"""
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    return graph