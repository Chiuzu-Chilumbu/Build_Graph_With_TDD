import pytest
from app.models.graph_adt import Graph
from app.models.queue_adt import Queue

# Marker for integrationt tests
pytestmark = pytest.mark.graph_integration_test

def test_bfs_with_queue(sample_graph):
    """Test BFS Traversal (Uses Queue ADT)"""
    traversal = sample_graph.bfs("A", queue_capacity=10)
    assert traversal == ["A", "B", "C", "D"]  # Expected BFS Order
