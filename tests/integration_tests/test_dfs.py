import pytest

# Marker for integration tests
pytestmark = pytest.mark.graph_integration_test

def test_dfs_with_stack(sample_graph):
    """Test DFS Traversal (Uses Stack ADT)"""
    traversal = sample_graph.dfs("A", stack_capacity=10)
    assert traversal == ["A", "C", "D", "B"]  