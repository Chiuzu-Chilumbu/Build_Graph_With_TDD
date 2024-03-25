"""Behavioural test to validate basic Queue operations"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from data.queue_adt import Queue

# Load scenarios from the feature file
scenarios('features/queue_operations.feature')



# Given Steps

@given('a new created queue object', target_fixture='queue')
def a_new_created_queue_object(new_queue):
    """a new created queue object."""
    return new_queue

@given('a queue with data in it')
def queue_with_data(new_queue):
    """We add test data to the queue"""
    new_queue.enqueue('test_data')  
    return new_queue


@given('a queue containing data with a certain size')
def queue_with_certain_size(new_queue):
    """Enqueue a known number of items"""
    for i in range(3):
        new_queue.enqueue(f'data_{i}')
    return new_queue


@given('a queue object contains no data')
def queue_with_no_data_in_it(new_queue):
    """enqueue and dequeue data"""
    new_queue.enqueue('data')
    new_queue.dequeue()
    return new_queue


@given('a queue where the size is equal to the given capacity')
def queue_at_full_capacity(new_queue):
    """enqueue data to full capacity"""
    for i in range(5):
        new_queue.enqueue(f'data_{i}')
    new_queue.show()
    return new_queue



# When Steps

@when('data is enqueued onto the queue')
def data_is_enqueued_onto_the_queue(new_queue):
    """data is enqueued onto the queue."""
    new_queue.enqueue('test_data')



@when('data is dequeued from the queue')
def dequeue_data(new_queue):
    """data us dequeued"""
    new_queue.dequeue()


@when('the size of the queue is checked')
def check_size(new_queue):
    """check queue size"""
    new_queue.size()


@when('the queue is checked if it is empty')
def check_if_queue_is_empty(new_queue):
    """check if queue is empty"""
    new_queue.isEmpty()


@when('the queue is checked if it is full')
def check_if_queue_is_Full(new_queue):
    """check if queue is full"""
    new_queue.isFull()



# Then Steps
    
@then('the data should be added onto the queue')
def the_data_should_be_added_onto_the_queue(new_queue):
    """the data should be added onto the queue."""
    assert new_queue.size() == 1


@then('the data should be removed from the queue')
def data_removed(new_queue):
    """Assuming 'test_data' was the only item; adjust assertion as needed"""
    assert new_queue.size() == 0, "Queue should be empty after dequeue."


@then('the queue should return the size of the queue which is equivalent to the number of data in the queue')
def size_returned(new_queue):
    """Here we directly assert in the When step"""
    assert new_queue.size() == 3, "Queue size should match the number of enqueued items."


@then('the queue should return True when empty')
def return_true_returned_when_empty(new_queue):
    """we assert the step action"""
    assert new_queue.isEmpty() is True


@then('the queue should return True when full')
def return_true_when_full(new_queue):
    """we assert the step action"""
    assert new_queue.isFull() is True