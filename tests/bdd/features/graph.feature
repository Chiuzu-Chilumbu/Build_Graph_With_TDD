# Feature file with the description of graph operation 

Feature: An instance of a Graph can be created and should be able to perform required operations
  
  Scenario: A Graph instance can be initialised from a class
    Given a graph class
    When an object is intanciated
    Then the graph should be created with an adjacency list representation