"""unit tests to validate basic Stack operations"""

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
        

def test_should_contain_no_elements_in_created_stack_list(new_stack):
    """Test to check if the stack object is created with an empty list"""
    assert new_stack.stack == []



def test_should_should_be_able_to_push_item_onto_stack_without_increasing_capacity(new_stack):
    """should be able to push an item onto the stack without increasing the capacity"""
    new_stack.push(5)
    # Assert
    assert new_stack.size() == 1
    assert new_stack.capacity == 5


def test_should_raise_exception_if_pushed_data_exceeds_stack_capacity(new_stack):
    """should raise an exception if pushed data exceeds stack capacity"""
    for i in range(1,6):
        new_stack.push(i)
        
    with pytest.raises(Exception):
        new_stack.push(0)


def test_should_pop_the_top_most_item_from_the_stack(new_stack):
    """should pop the top most item from the stack"""
    new_stack.push(5)
    new_stack.push(4)
    new_stack.pop()
    
    assert new_stack.peek() == 5
    assert new_stack.size() == 1


def test_should_raise_an_exception_when_pop_operation_is_used_on_empty_list(new_stack):
    """should raise an exception when pop operation is used on an empty list"""
    with pytest.raises(Exception):
        new_stack.pop()


def test_should_return_true_if_stack_is_full(new_stack):
    """should return True if the stack is full"""
    for values in range(1, 6):
        new_stack.push(values)

    # assert
    assert new_stack.isFull() == True


def test_should_return_false_if_the_stack_is_not_full(new_stack):
    """should return False if the stack is not full"""
    for values in range(1, 5):
        new_stack.push(values)
        
    assert new_stack.isFull() == False


def test_should_return_true_if_stack_is_empty(new_stack):
    """should return True if the stack is empty"""
    assert new_stack.isEmpty() == True


def test_should_return_false_if_stack_is_not_empty(new_stack):
    """should return False if the stack is not empty"""
    new_stack.push(5)
    assert new_stack.isEmpty() == False