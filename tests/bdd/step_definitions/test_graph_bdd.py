"""Behavioural steps to validate basic Graph operations"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from collections import defaultdict

# pytest marker for graph BDD tests
pytestmark = pytest.mark.graph_bdd_test

scenarios('../features/graph.feature')

# Given step
@given('a graph class')
def should_contain_graph_class(new_graph):
    return new_graph

# When steps
@when('an object is instantiated')
def create_graph_object_instance():
    pass


@when(parsers.parse('a vertex "{vertex}" is added'))
def add_vertex(new_graph, vertex):
    vertex = vertex.strip().replace('"', '')  # ✅ Remove any extra quotes
    new_graph.add_vertex(vertex)



@when(parsers.parse('an edge is added between "{v1}" and "{v2}"'))
def add_edges(new_graph, v1, v2):
    v1 = v1.strip().replace('"', '')  # ✅ Remove quotes
    v2 = v2.strip().replace('"', '')  # ✅ Remove quotes

    #print(f"DEBUG: Adding edge between {v1} and {v2}")  # ✅ Debugging
    new_graph.add_edge(v1, v2)
    #print("DEBUG: Graph after adding edge:", new_graph.adjList)  # ✅ Debugging



@when(parsers.parse("BFS is performed starting from \"{start_vertex}\""), target_fixture="bfs_traversal")
def perform_bfs(new_graph, start_vertex):
    return new_graph.bfs(start_vertex)


@when(parsers.parse("DFS is performed starting from \"{start_vertex}\""), target_fixture="dfs_traversal")
def perform_dfs(new_graph, start_vertex):
    return new_graph.dfs(start_vertex) 


#Then steps

@then('the graph should be created with an adjacency list representation')
def adjacency_list_graph_representation_is_created(new_graph):
    assert isinstance(new_graph.adjList, defaultdict)


@then(parsers.parse('the graph should contain vertex "{vertex}"'))
def graph_should_contain_vertex(new_graph, vertex):
    assert vertex in new_graph.adjList



@then(parsers.parse('vertex "{neighbour}" should be a neighbour of "{vertex}"'))
def vertex_should_be_neighbour(new_graph, vertex, neighbour):
    vertex = vertex.strip().replace('"', '')  # ✅ Fix potential quote issues
    neighbour = neighbour.strip().replace('"', '')  # ✅ Fix potential quote issues

    #print("DEBUG: Current Graph Adjacency List:", new_graph.adjList)  # ✅ Debugging
    assert neighbour in new_graph.adjList[vertex], f"Expected {neighbour} in {new_graph.adjList[vertex]}"


# @then(parsers.parse('the BFS traversal should be "{expected_traversal}"'))
# def bfs_traversal_should_match(bfs_traversal, expected_traversal):
#     assert " ".join(bfs_traversal) == expected_traversal



# @then(parsers.parse('the DFS traversal should be {expected_traversal}'))
# def dfs_traversal_should_match(dfs_traversal, expected_traversal):
#     assert " ".join(dfs_traversal) == expected_traversal