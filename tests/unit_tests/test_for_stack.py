"""unit tests designed to test the basic operations of a stack abstract data type"""

from data.stack_adt import Stack
import pytest



def test_should_create_instance_of_stack_with_given_capacity():
    """Test to check if the stack object is created with the given capacity"""
    size = 100
    stack_object = Stack(size)
    assert stack_object.capacity == 100


def test_should_provide_capacity_only_with_int_data_type():
    """Test to check if the stack object is created with the given capacity"""
    bad_size = "one_hundred"
    with pytest.raises(TypeError):
        stack_object = Stack(bad_size)
        

def test_should_contain_no_elements_in_created_stack_list():
    """Test to check if the stack object is created with an empty list"""
    stack_object = Stack(100)
    assert stack_object.stack == []


@pytest.fixture(scope='function')
def stack_object_instance():
    """fixture to provide a stack object for each test"""
    stack = Stack(100)
    return stack


def test_should_should_be_able_to_push_item_onto_stack_without_increasing_capacity(
        stack_object_instance):
    """should be able to push an item onto the stack without increasing the capacity"""
    stack_object_instance.push(5)
    # Assert
    assert stack_object_instance.size() == 1
    assert stack_object_instance.capacity == 100


def test_should_raise_exception_if_pushed_data_exceeds_stack_capacity(
        stack_object_instance):
    """should raise an exception if pushed data exceeds stack capacity"""
    for i in range(100):
        stack_object_instance.push(i)
        
    with pytest.raises(Exception):
        stack_object_instance.push(101)


def test_should_pop_the_top_most_item_from_the_stack(stack_object_instance):
    """should pop the top most item from the stack"""
    stack_object_instance.push(5)
    stack_object_instance.push(4)
    stack_object_instance.pop()
    
    assert stack_object_instance.peek() == 5
    assert stack_object_instance.size() == 1


def test_should_raise_an_exception_when_pop_operation_is_used_on_empty_list(
        stack_object_instance):
    """should raise an exception when pop operation is used on an empty list"""
    with pytest.raises(Exception):
        stack_object_instance.pop()


def test_should_return_true_if_stack_is_full(stack_object_instance):
    """should return True if the stack is full"""
    for values in range(1, 101):
        stack_object_instance.push(values)

    # assert
    assert stack_object_instance.isFull


def test_should_return_false_if_the_stack_is_not_full(stack_object_instance):
    """should return False if the stack is not full"""
    for values in range(1, 100):
        stack_object_instance.push(values)
        
    stack_object_instance.isFull == False


def test_should_return_true_if_stack_is_empty(stack_object_instance):
    """should return True if the stack is empty"""
    assert stack_object_instance.isEmpty()


def test_should_return_false_if_stack_is_not_empty(stack_object_instance):
    """should return False if the stack is not empty"""
    stack_object_instance.push(5)
    assert stack_object_instance.isEmpty() == False