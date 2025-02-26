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



def test_dequeue_from_queue(queue_page):
    """Test dequeue operation"""
    queue_page.set_queue_capacity(5)  # ✅ Reset queue

    # ✅ Fill queue first
    for i in range(5):
        queue_page.enqueue_item(i)

    # ✅ Dequeue one item
    queue_page.dequeue_item()

    # ✅ Fetch updated queue items **immediately**
    final_items = queue_page.get_queue_items()

    # ✅ Queue should have one less item
    assert len(final_items) == 4



def test_dequeue_empty_queue(queue_page):
    """Test dequeue operation when queue is empty"""
    queue_page.set_queue_capacity(5)  # ✅ Reset queue

    # ✅ Attempt one more dequeue beyond empty state
    queue_page.dequeue_item()

    # ✅ Assert correct error message
    assert "Queue is empty" in queue_page.get_status_message()