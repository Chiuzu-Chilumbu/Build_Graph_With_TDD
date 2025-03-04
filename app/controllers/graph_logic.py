from flask import jsonify, request
from app.models.graph_adt import Graph

# Use a single global Graph instance to persist data
graph_instance = Graph()

class GraphController:
    def __init__(self):
        self.graph = graph_instance  # Use a persistent graph instance

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        self.graph.add_vertex(vertex)
        return jsonify({
            'success': True,
            'message': f'Vertex {vertex} added',
            'result': self.graph.get_graph()
        }), 200

    def add_edge(self, v1, v2):
        """Add an edge between two vertices"""
        self.graph.add_edge(v1, v2)
        return jsonify({
            'success': True,
            'message': f'Edge added between {v1} and {v2}',
            'result': self.graph.get_graph()
        }), 200

    def get_graph_data(self):
        """Return the graph structure"""
        return jsonify({
            'success': True,
            'result': self.graph.get_graph()
        }), 200

    def bfs_traversal(self, start_vertex):
        """Perform BFS traversal and return the result"""
        if start_vertex not in self.graph.adjList:
            return jsonify({
                'success': False,
                'message': f'Vertex {start_vertex} not found in graph.'
            }), 400

        traversal = self.graph.bfs(start_vertex)
        return jsonify({
            'success': True,
            'message': f'BFS traversal from {start_vertex}',
            'traversal': traversal
        }), 200

    def dfs_traversal(self, start_vertex):
        """Perform DFS traversal and return the result"""
        if start_vertex not in self.graph.adjList:
            return jsonify({
                'success': False,
                'message': f'Vertex {start_vertex} not found in graph.'
            }), 400

        traversal = self.graph.dfs(start_vertex)
        return jsonify({
            'success': True,
            'message': f'DFS traversal from {start_vertex}',
            'traversal': traversal
        }), 200
