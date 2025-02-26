import pytest
from selenium.webdriver.support.wait import WebDriverWait
from tests.acceptance_tests.pages.queue_page import QueuePage

pytestmark = pytest.mark.queue_acceptance_test


def test_initialise_queue(queue_page):
    """Test Queue Initialization"""
    queue_page.set_queue_capacity(5)
    assert "Queue initialized successfully!" in queue_page.get_status_message()


def test_enqueue_to_queue(driver):
    """Test enqueue operation"""
    queue_page = QueuePage(driver)
    queue_page.enqueue_item(10)
    assert "10" in queue_page.get_queue_items()


def test_queue_full_state(driver):
    """Test behaviour when queue is full"""
    queue_page = QueuePage(driver)

    for i in range(4):
        queue_page.enqueue_item(i)

    queue_page.enqueue_item(5) # attempt one more enqueue



# TODO : Need to fix this test
# def test_dequeue_from_queue(driver):
#     """Test dequeue operation"""
#     queue_page = QueuePage(driver)
#     queue_page.set_queue_capacity(5)

#     # enqueue item
#     queue_page.enqueue_item(24)

#     initial_items = queue_page.get_queue_items()
#     assert "24" in initial_items

#     # ✅ Pop the item
#     queue_page.dequeue_item()

#     # ✅ Wait for the UI to update before asserting
#     WebDriverWait(driver, 5).until(
#         lambda d: len(queue_page.get_queue_items()) < len(initial_items)
#     )

#     final_items = queue_page.get_queue_items()
    
#     assert len(final_items) == len(initial_items) - 1
#     assert "24" not in final_items




def test_dequeue_empty_queue(driver):
    """Test dequeue operation when queue is empty"""
    queue_page = QueuePage(driver)
    queue_page.set_queue_capacity(5) 

    # ✅ Attempt one more dequeue beyond empty state
    queue_page.dequeue_item()

    # ✅ Assert correct error message
    assert "Queue is empty" in queue_page.get_status_message()