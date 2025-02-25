"""unit tests to validate basic Graph operations"""

import pytest
from collections import defaultdict
from app.models.graph_adt import Graph

# marker for graph unit tests
pytestmark = pytest.mark.graph_unit_test

def test_graph_should_be_represented_by_adjacency_list(new_graph):
    # Act, Arrange, Assert
    assert isinstance(new_graph.adjList, defaultdict)


def test_add_vertex(new_graph):
    new_graph.add_vertex("A")
    assert "A" in new_graph.adjList


def test_add_edge(new_graph):
    new_graph.add_vertex("A")
    new_graph.add_vertex("B")
    new_graph.add_edge("A", "B")
    assert "B" in new_graph.adjList["A"]
    assert "A" in new_graph.adjList["B"]