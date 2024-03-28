"""Behavioral test to test the basic stack operations"""

import pytest
from pytest_bdd import scenarios, given, when, then


# Scenarios
scenarios('../features/stack.feature')


# Given Steps
@given('a stack class exists')
def stack_class(new_stack):
    """new stack"""
    return new_stack


@given('a stack object with provided capacity')
def stack_with_capacity(new_stack):
    """we create a stack object with a given capacity"""
    return new_stack


@given('an already created stack object with some data')
def stack_with_data(new_stack):
    """we create a stack object with some data in it"""
    new_stack.push(10)
    new_stack.push(20)
    return new_stack


@given('a new stack object with provided capacity')
def new_stack_with_capacity(new_stack):
    """we create a new stack object with a given capacity"""
    return new_stack


@given('a stack object with given capacity')
def stack_with_given_capacity(new_stack):
    """we create a stack object with a given capacity"""
    return new_stack


# When steps

@when('a stack object is instantiated with the stack capacity')
def stack_object():
    """we create a stack object with the given capacity"""
    pass

@when('the data is pushed onto the stack')
def push_data_onto_stack(new_stack):
    """we push data onto the stack object"""
    new_stack.push(10)


@when('the top data is popped from the stack')
def pop_data_from_stack(new_stack):
    """we pop data from the stack object"""
    new_stack.pop()


@when('no data has been entered into the stack')
def no_data_entered(new_stack):
    """we create a stack object with capacity 5"""
    return new_stack


@when('the capacity amount of data is pushed onto the stack')
def push_data_to_full(new_stack):
    """we push data onto the stack object until it is full"""
    for i in range(5):
        new_stack.push(i)


# Then Steps
@then('the instantiated stack object should contain an empty list')
def stack_with_full_given_capacity(new_stack):
    """Test to check if the stack as 100 capacity as given"""
    assert new_stack.capacity == 5


@then('the data pushed should be seen or peeked as the most recent data')
def verify_data_pushed(new_stack):
    """Test to check if the data pushed is the most recent data in the stack"""
    assert new_stack.peek() == 10


@then('the stack should have one less item and return the popped data')
def verify_data_popped(new_stack):
    """Test to check if the data popped is the most recent data in the stack"""
    assert new_stack.peek() == 10
    assert new_stack.size() == 1


@then('the stack should be empty')
def verify_stack_empty(new_stack):
    """stack should be empty"""
    assert new_stack.isEmpty()


@then('the stack should be full and not allow new data to be pushed')
def verify_stack_full(new_stack):
    """raise exception"""
    with pytest.raises(Exception):
        new_stack.push(6)
    assert new_stack.isFull()
