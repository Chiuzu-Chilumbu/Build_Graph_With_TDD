"""Behavioural steps to validate basic Graph operations"""
import pytest
from pytest_bdd import scenarios, given, when, then
from collections import defaultdict

# pytest marker for graph BDD tests
pytestmark = pytest.mark.graph_bdd_test

scenarios('../features/graph.feature')

# Given step
@given('a graph class')
def should_contain_graph_class(new_graph):
    return new_graph

# When and Then steps
@when('an object is instantiated')
def create_graph_object_instance():
    pass

@then('the graph should be created with an adjacency list representation')
def adjacency_list_graph_representation_is_created(new_graph):
    assert isinstance(new_graph.adjList, defaultdict)
