import pytest
from selenium.webdriver.support.ui import WebDriverWait
from tests.acceptance_tests.pages.queue_page import QueuePage

pytestmark = pytest.mark.queue_acceptance_test




def test_initialise_queue(queue_page):
    """Test Queue Initialization"""
    queue_page.set_queue_capacity(5)
    assert "Queue initialized successfully!" in queue_page.get_status_message()


def test_enqueue_to_queue(queue_page):
    """Test enqueue operation"""
    queue_page.enqueue_item(10)
    assert "10" in queue_page.get_queue_items()


def test_queue_full_state(queue_page):
    """Test behaviour when queue is full"""
    for i in range(4):
        queue_page.enqueue_item(i)

    queue_page.enqueue_item(5) # attempt one more enqueue


# TODO: Fix dequeue from queue tests 

# def test_dequeue_from_queue(queue_page):
#     """Test dequeue operation"""
#     queue_page.dequeue_item()

#     # Wait for UI to update
#     WebDriverWait(queue_page.driver, 5).until(
#         lambda d: len(queue_page.get_queue_items()) < 5
#     )

#     assert len(queue_page.get_queue_items()) == 4


# def test_dequeue_empty_queue(queue_page):
#     """Test dequeue operation when queue is empty"""
#     for _ in range(4):  # Empty the queue
#         queue_page.dequeue_item()

#     queue_page.dequeue_item()  # One more dequeue beyond empty state

#     assert "Queue is empty" in queue_page.get_status_message()