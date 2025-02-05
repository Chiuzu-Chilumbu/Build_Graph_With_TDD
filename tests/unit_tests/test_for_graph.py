"""unit tests to validate basic Graph operations"""

from app.models.graph_adt import Graph
import pytest
from collections import defaultdict

# marker for graph unit tests
pytestmarker = pytest.mark.graph_unit_test

def test_graph_should_be_represented_by_adjacency_list(new_graph):
    # Act, Arrange, Assert
    assert isinstance(new_graph.adjList, defaultdict)
