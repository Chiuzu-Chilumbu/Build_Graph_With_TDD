"""Behavioral test to test the basic stack operations"""

import pytest
from pytest_bdd import scenarios, given, when, then
from data.stack_adt import Stack


# Scenarios
scenarios('../features/stack.feature')


# Given Steps
@given('a stack class exists')
def stack_class(new_stack):
    return new_stack


@given('a stack object with provided capacity')
def stack_with_capacity():
    """we create a stack object with a given capacity"""
    return Stack(50)


@given('an already created stack object with some data')
def stack_with_data():
    """we create a stack object with some data in it"""
    stack = Stack(50)
    stack.push(10)
    stack.push(20)
    return stack


@given('a new stack object with provided capacity')
def new_stack_with_capacity():
    """we create a new stack object with a given capacity"""
    return Stack(50)


@given('a stack object with given capacity')
def stack_with_given_capacity():
    """we create a stack object with a given capacity"""
    return Stack(5)


# When steps

@when('a stack object is instantiated with the stack capacity')
def stack_object(stack_class):
    """we create a stack object with the given capacity"""
    return stack_class(100)

@when('the data is pushed onto the stack')
def push_data_onto_stack(stack_with_capacity):
    """we push data onto the stack object"""
    stack_with_capacity.push(10)


@when('the top data is popped from the stack')
def pop_data_from_stack(stack_with_data):
    """we pop data from the stack object"""
    stack_with_data.pop()


@when('no data has been entered into the stack')
def no_data_entered(new_stack_with_capacity):
    """we create a stack object with capacity 5"""
    return new_stack_with_capacity


@when('the capacity amount of data is pushed onto the stack')
def push_data_to_full(stack_with_given_capacity):
    """we push data onto the stack object until it is full"""
    for i in range(5):
        stack_with_given_capacity.push(i)


# Then Steps
        
@then('the instantiated stack object should contain an empty list')
def test_stack_with_given_capacity(stack_object):
    """Test to check if the stack as 100 capacity as given"""
    assert stack_object.capacity == 100


@then('the data pushed should be seen or peeked as the most recent data')
def verify_data_pushed(stack_with_capacity):
    """Test to check if the data pushed is the most recent data in the stack"""
    assert stack_with_capacity.peek() == 10


@then('the stack should have one less item and return the popped data')
def verify_data_popped(stack_with_data):
    """Test to check if the data popped is the most recent data in the stack"""
    assert stack_with_data.peek() == 10
    assert stack_with_data.size() == 1


@then('the stack should be empty')
def verify_stack_empty(new_stack_with_capacity):
    assert new_stack_with_capacity.isEmpty()


@then('the stack should be full and not allow new data to be pushed')
def verify_stack_full(stack_with_given_capacity):
    with pytest.raises(Exception):
        stack_with_given_capacity.push(6)
    assert stack_with_given_capacity.isFull()
