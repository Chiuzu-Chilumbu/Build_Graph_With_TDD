"""conftest file that holds all needed pytest fixtures"""

import pytest
from data.queue_adt import Queue
from data.stack_adt import Stack

@pytest.fixture(scope='function')
def new_queue():
	"""fixture to provide a new queue for each test"""
	return Queue(5)



@pytest.fixture(scope='function')
def new_stack():
	"""fixture to provide a new queue for each test"""
	return Stack

