"""unit tests designed to test the basic operations of a stack abstract data type"""

from data.stack_adt import Stack

import pytest
from data.stack_adt import Stack


@pytest.fixture(scope='function')
def stack_object_instance():
    stack = Stack(100)
    return stack


def test_should_should_be_able_to_push_item_onto_stack_without_increasing_capacity(
        stack_object_instance):
    #  Arrange & Act
    stack_object_instance.push(5)
    # Assert
    assert stack_object_instance.size() == 1
    assert stack_object_instance.capacity == 100


def test_should_raise_exception_if_pushed_data_exceeds_stack_capacity(
        stack_object_instance):
    #  Arrange & Act
    for i in range(100):
        stack_object_instance.push(i)

    #  Assert
    with pytest.raises(Exception):
        stack_object_instance.push(101)


def test_should_pop_the_top_most_item_from_the_stack(stack_object_instance):
    # Arrange
    stack_object_instance.push(5)
    stack_object_instance.push(4)
    #  Act
    stack_object_instance.pop()
    # assert
    stack_object_instance.peek() == 5
    stack_object_instance.size() == 1


def test_should_raise_an_exception_when_pop_operation_is_used_on_empty_list(
        stack_object_instance):
    # Arrange & Act and Assert
    with pytest.raises(Exception):
        stack_object_instance.pop()


def test_should_return_true_if_stack_is_full(stack_object_instance):
    # arrange & act
    for values in range(1, 101):
        stack_object_instance.push(values)

    # assert
    stack_object_instance.isFull


def test_should_return_false_if_the_Stack_is_not_full(stack_object_instance):
    # arrange & act
    for values in range(1, 100):
        stack_object_instance.push(values)

    # assert
    stack_object_instance.isFull == False


def test_should_return_true_if_stack_is_empty(stack_object_instance):
    # arrange, act and assert
    assert stack_object_instance.isEmpty()


def test_should_return_false_if_stack_is_not_empty(stack_object_instance):
    # arrange & act
    stack_object_instance.push(5)
    # assert
    assert stack_object_instance.isEmpty() == False