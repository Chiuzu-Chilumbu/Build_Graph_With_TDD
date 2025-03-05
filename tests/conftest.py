"""conftest file that holds all needed pytest fixtures"""

import pytest
from app.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.acceptance_tests.pages.stack_page import StackPage
from tests.acceptance_tests.pages.queue_page import QueuePage
from tests.acceptance_tests.pages.graph_page import GraphPage
from app.models.queue_adt import Queue
from app.models.stack_adt import Stack
from app.models.graph_adt import Graph


# Base URL Fixture
# @pytest.fixture(scope="session")
# def base_url():
#     """Return the correct base URL depending on the environment"""
#     environment = os.getenv("ENVIRONMENT", "development")  # Defaults to "development"
#     if environment == "production":
#         return "https://your-heroku-app.herokuapp.com"  # Replace with your Heroku app URL
#     return "http://localhost:5001"  # Default to local testing



@pytest.fixture(scope="session")
def base_url():
    """Return the correct base URL depending on the environment"""
    return Config.BASE_URL  # Use the BASE_URL from Flask config


# Fixtures for Queue, Stack, and Graph
@pytest.fixture(scope='function')
def new_queue():
	"""Fixture to provide a new queue for each test"""
	return Queue(5)

@pytest.fixture(scope='function')
def new_stack():
	"""Fixture to provide a new stack for each test"""
	return Stack(5)

@pytest.fixture(scope='function')
def new_graph():
	"""Fixture to provide a new graph for each test"""
	return Graph()

@pytest.fixture(scope="function")
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


# WebDriver Fixture (Selenium)
@pytest.fixture(scope="module")
def driver():
	"""Set up WebDriver for Chrome (Reusable for all tests)"""
	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	yield driver
	driver.quit()


# StackPage Fixtures Using `base_url`
@pytest.fixture(scope="module")
def stack_page(driver, base_url):
    """Navigate to Stack page and return StackPage Object"""
    driver.get(f"{base_url}/stack") 
    return StackPage(driver)


# QueuePage Fixtures Using `base_url
@pytest.fixture(scope="module")
def queue_page(driver, base_url):
    """Navigate to Queue page and return QueuePage Object"""
    driver.get(f"{base_url}/queue") 
    return QueuePage(driver)



# GraphPage Fixtures Using `base_url
@pytest.fixture(scope="module")
def graph_page(driver, base_url):
    """Navigate to Graph page and return GraphPage Object"""
    driver.get(f"{base_url}/graph")  
    return GraphPage(driver)


@pytest.fixture(scope="module")
def clear_graph(driver, base_url):
    """Clears all vertices and edges before running a test."""
    driver.get(f"{base_url}/graph")  # ✅ Reload the graph page
    driver.execute_script("localStorage.clear();")  # ✅ Clear localStorage
    driver.refresh()  # ✅ Refresh to apply changes
