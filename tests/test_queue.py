"""Unit test for individual components of the queue class"""

from queue.queue_adt import Queue


def test_should_create_a_queue_object_from_queue_class(new_queue):
    """a class called Queue."""
    assert new_queue is not None
    assert isinstance(new_queue, Queue)
