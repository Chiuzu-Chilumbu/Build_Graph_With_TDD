"""Creating a stack Feature"""

Feature: Design a stack abstract datatype class

  Scenario: Create a stack object from a stack class
    Given a stack class exists
    When a stack object is instantiated with the stack capacity
    Then the instantiated stack object should contain an empty list
