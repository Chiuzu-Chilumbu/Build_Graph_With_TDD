"""Feature file to ensure stack operations"""

Feature: After having created the stack, we should be able to perform basic stack operations

  Scenario: the stack class object should be able to push data onto the created list
    Given a stack object with provided capacity
    When the data is pushed onto the stack
    Then the data pushed should be seen or peeked as the most recent data

  Scenario: The stack class should be able to pop data from the created stack list
    Given an already created stack object with some data
    When the top data is popped from the stack
    Then the stack should have one less item and return the popped data

  Scenario: The stack class should be able to check if the stack is empty
    Given a new stack object with provided capacity
    When no data has been entered into the stack
    Then the stack should be empty

  Scenario: the stack class should be able to check if the stack is full
    Given a stack object with given capacity
    When the capacity amount of data is pushed onto the stack
    Then the stack should be full and not allow new data to be pushed
