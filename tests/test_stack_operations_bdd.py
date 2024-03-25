"""Behavioral test to test the basic stack operations"""
from data.stack_adt import Stack

import pytest
from pytest_bdd import scenarios, given, when, then


scenarios('features/stack_operations.feature')


@pytest.fixture(scope='function')
@given('a stack object with provided capacity')
def stack_with_capacity():
    return Stack(50)


@pytest.fixture(scope='function')
@given('an already created stack object with some data')
def stack_with_data():
    stack = Stack(50)
    stack.push(10)
    stack.push(20)
    return stack


@pytest.fixture(scope='function')
@given('a new stack object with provided capacity')
def new_stack_with_capacity():
    return Stack(50)


@pytest.fixture(scope='function')
@given('a stack object with given capacity')
def stack_with_given_capacity():
    return Stack(5)


@when('the data is pushed onto the stack')
def push_data_onto_stack(stack_with_capacity):
    stack_with_capacity.push(10)


@when('the top data is popped from the stack')
def pop_data_from_stack(stack_with_data):
    stack_with_data.pop()


@when('no data has been entered into the stack')
def no_data_entered(new_stack_with_capacity):
    pass


@when('the capacity amount of data is pushed onto the stack')
def push_data_to_full(stack_with_given_capacity):
    for i in range(5):
        stack_with_given_capacity.push(i)


@then('the data pushed should be seen or peeked as the most recent data')
def verify_data_pushed(stack_with_capacity):
    assert stack_with_capacity.peek() == 10


@then('the stack should have one less item and return the popped data')
def verify_data_popped(stack_with_data):
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
