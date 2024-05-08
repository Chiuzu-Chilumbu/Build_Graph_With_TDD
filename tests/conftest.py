"""conftest file that holds all needed pytest fixtures"""

import pytest
from data.queue_adt import Queue
from data.stack_adt import Stack
from data.graph_adt import Graph

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