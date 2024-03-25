"""conftest file that holds all needed pytest fixtures"""

import pytest 
from queue.queue_adt import Queue

@pytest.fixture(scope='function')
def new_queue():
	"""fixture to provide a new queue for each test"""
	return Queue(5)

