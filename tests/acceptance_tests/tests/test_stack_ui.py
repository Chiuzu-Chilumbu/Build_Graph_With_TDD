import pytest
from tests.acceptance_tests.pages.stack_page import StackPage

pytestmark = pytest.mark.stack_acceptance_test


def test_initialize_stack(stack_page):
    """Test Stack Initialisation with a valid capacity"""
    stack_page.set_stack_capacity(5)
    assert "Stack initialized successfully!" in stack_page.get_status_message()


def test_push_to_stack(driver):
    """Testing Pushing items to the stack"""
    stack_page = StackPage(driver)
    stack_page.push_item(1)

    assert '1' in stack_page.get_stack_items()
    assert stack_page.is_pop_button_enabled() # Pop button should be enabled after pushing


def test_stack_full_state(driver):
    """Test stack full behavior by asserting error message when stack is full"""
    stack_page = StackPage(driver)

    for i in range(5):  # Push until full
        stack_page.push_item(i)

    # ✅ Attempt one more push beyond capacity
    stack_page.push_item(6)

    # ✅ Assert we get the expected "Stack is full" message
    assert "Stack is full" in stack_page.get_status_message()



def test_pop_from_stack(driver):
    """Test popping items from the stack"""
    stack_page = StackPage(driver)
    stack_page.set_stack_capacity(5)

    # ✅ Push an item
    stack_page.push_item(42)
    initial_items = stack_page.get_stack_items()
    assert "42" in initial_items

    # ✅ Pop the item
    stack_page.pop_item()

    final_items = stack_page.get_stack_items()
    
    assert len(final_items) == len(initial_items) - 1
    assert "42" not in final_items



def test_pop_empty_stack(driver):
    """Test Popping fom an empty stack"""
    stack_page = StackPage(driver)
    stack_page.set_stack_capacity(5)

    for _ in range(4):  # Empty the stack
        stack_page.pop_item()

    stack_page.pop_item()
    assert "Cannot pop from empty stack" in stack_page.get_status_message()
