import pytest 
from tests.acceptance_tests.pages.stack_page import StackPage

pytestmark = pytest.mark.stack_acceptance_test

@pytest.fixture(scope="module")
def stack_page(driver):
    """navigate to Stack page and return StackPage Object"""
    driver.get("http://127.0.0.1:5001/stack")
    return StackPage(driver)


def test_initialize_stack(stack_page):
    """Test Stack Initialisation with a valid capacity"""
    stack_page.set_stack_capacity(5)
    assert "Stack initialized successfully!" in stack_page.get_status_message()