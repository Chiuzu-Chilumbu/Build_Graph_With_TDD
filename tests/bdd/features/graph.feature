Feature: Graph operations including adding vertices, edges, and performing traversals
  
  Scenario: A Graph instance can be initialized from a class
    Given a graph class
    When an object is instantiated
    Then the graph should be created with an adjacency list representation

  Scenario: A vertex can be added to the graph
    Given a graph class
    When a vertex "A" is added
    Then the graph should contain vertex "A"

  Scenario: An edge can be added between two vertices
    Given a graph class
    When a vertex "A" is added
    And a vertex "B" is added
    And an edge is added between "A" and "B"
    Then vertex "B" should be a neighbour of "A"
    And vertex "A" should be a neighbour of "B"



#   Scenario: Perform BFS traversal on a graph
#     Given a graph class
#     When a vertex "A" is added
#     And a vertex "B" is added
#     And a vertex "C" is added
#     And an edge is added between "A" and "B"
#     And an edge is added between "A" and "C"
#     And BFS is performed starting from "A"
#     Then the BFS traversal should be "A B C"

#   Scenario: Perform DFS traversal on a graph
#     Given a graph class
#     When a vertex "A" is added
#     And a vertex "B" is added
#     And a vertex "C" is added
#     And an edge is added between "A" and "B"
#     And an edge is added between "A" and "C"
#     And DFS is performed starting from "A"
#     Then the DFS traversal should be "A C B"
