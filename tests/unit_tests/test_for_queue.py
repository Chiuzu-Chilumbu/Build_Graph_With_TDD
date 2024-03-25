"""unit tests to validate basic Queue operations"""

import pytest
from data.queue_adt import Queue

def test_should_create_a_queue_object_from_queue_class(new_queue):
    """a class called Queue."""
    assert new_queue is not None
    assert isinstance(new_queue, Queue)

def test_queue_is_initially_empty(new_queue):
    """Test if a new queue is initially empty."""
    assert new_queue.size() == 0, "New queue should be empty."

def test_queue_enqueues_correctly(new_queue):
    """Test if an item is correctly enqueued to the queue."""
    new_queue.enqueue('item')
    assert new_queue.size() == 1, "Queue should have one item after enqueue."
    assert 'item' == new_queue.queue[0], "Enqueued item should be in the queue."

def test_queue_multiple_enqueues(new_queue):
    """Test if multiple items are correctly enqueued to the queue."""
    items = ['item1', 'item2', 'item3']
    for item in items:
        new_queue.enqueue(item)
    assert new_queue.size() == len(items), "Queue size should equal the number of enqueued items."
    for i, item in enumerate(items):
        assert item == new_queue.queue[i], f"Item {i} in the queue should be {item}."


def test_queue_is_not_empty_after_enqueue(new_queue):
    """Test if the queue is not empty after an enqueue operation."""
    new_queue.enqueue(1)
    assert new_queue.isEmpty() is False, "Queue should not be empty after enqueue operation"


def test_queue_is_full(new_queue):
    """Test if the queue is full when enqueued to its capacity."""
    for i in range(5):  
        new_queue.enqueue(i)
    assert new_queue.isFull() is True, "Queue should be full when enqueued to capacity"


def test_enqueue_on_full_queue_raises_exception(new_queue):
    """Test if enqueuing on a full queue raises an exception."""
    for i in range(5):  
        new_queue.enqueue(i)
    with pytest.raises(Exception) as e:
        new_queue.enqueue(4)
    assert str(e.value) == "Queue is Full"

def test_dequeue_on_empty_queue_raises_exception(new_queue):
    """Test if dequeuing on an empty queue raises an exception."""
    with pytest.raises(Exception) as e:
        new_queue.dequeue()
    assert str(e.value) == "Queue is empty"


def test_queue_is_not_full_after_dequeue(new_queue):
    """Test if the queue is not full after a dequeue operation."""
    for i in range(5):
        new_queue.enqueue(i)
    new_queue.dequeue()  # Remove one item
    assert new_queue.isFull() is False, "Queue should not be full after dequeue operation"


def test_queue_becomes_empty_after_clearing(new_queue):
    """Test if the queue becomes empty after removing all items."""
    for i in range(5):  
        new_queue.enqueue(i)
    for _ in range(5): 
        new_queue.dequeue()
    assert new_queue.isEmpty() is True, "Queue should be empty after removing all items"


def test_peek_operation(new_queue):
    """Test the peek operation."""
    new_queue.enqueue('peek_item')
    assert new_queue.peek() == 'peek_item', "Peek should return the first item without removing it."
    assert new_queue.size() == 1, "Queue size should not change after peek operation."









