"""Test steps for testing the Queue class with BDD"""

from data.queue_adt import Queue
from pytest_bdd import scenario, given, when, then


@scenario('features/create_queue.feature',
          'A queue object should be created from the queue class')
def instantiate_a_queue_object_from_queue_class():
    """A queue object should be created from the queue class."""
    pass


@given('a class called Queue')
def should_contain_a_queue_class():
    """a class called Queue."""
    pass


@when('an object is instantiated from the Queue class')
def test_object_should_be_created_from_queue_class(new_queue):
    """an object is instantiated from the Queue class."""
    assert new_queue is not None


@then('The object should be an instance of the queue class')
def test_created_object_should_be_instance_of_queue_class(new_queue):
    """The object should be an instance of the queue class."""
    assert isinstance(new_queue, Queue)
