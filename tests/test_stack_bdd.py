"""Behavioral tests for stack abstract datatype"""

from data.stack_adt import Stack

import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('features/create_stack.feature')


@pytest.fixture
@given('a stack class exists')
def stack_class():
    return Stack


@pytest.fixture
@when('a stack object is instantiated with the stack capacity')
def stack_object(stack_class):
    return stack_class(100)


@then('the instantiated stack object should contain an empty list')
def test_stack_with_given_capacity(stack_object):
    assert stack_object.capacity == 100