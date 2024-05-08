"""unit tests to validate basic Graph operations"""

from data.graph_adt import Graph
import pytest
from collections import defaultdict

def test_graph_should_be_represented_by_adjacency_list(new_graph):
    # Act, Arrange, Assert
    assert new_graph.AdjList == type(defaultdict)
