"""In this module we will implement our graph representation using an adjacency list"""
from collections import defaultdict
import dataclasses


@dataclasses.dataclass
class vertex:
    name: str


class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_vertex(self, value):
        raise NotImplementedError