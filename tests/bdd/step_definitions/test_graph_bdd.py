"""Behavioural steps to validate basic Graph operations"""

import pytest
from pytest_bdd import scenarios, given, when, then
from data.graph_adt import Graph
from collections import defaultdict

scenarios('../features/graph.feature')

# Given step
@given('a graph class')
def should_contain_graph_class(new_graph):
    return new_graph


# Then step
@when('an object is intanciated')
def create_graph_object_instance():
    pass


@then('the graph should be created with an adjacency list representation')
def adjacenecy_list_graph_representation_is_created(new_graph):
    assert type(new_graph.adjList) is defaultdict