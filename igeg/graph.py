from typing import Dict, List

from .node import IGEGNode

from .edge import IGEGEdge


class IGEGGraph:

    def __init__(self):

        self.nodes: Dict[str, IGEGNode] = {}

        self.edges: List[IGEGEdge] = []

    def add_node(self, node: IGEGNode):

        self.nodes[node.id] = node

        return node.id

    def add_edge(self, edge: IGEGEdge):

        self.edges.append(edge)

    def get_node(self, node_id):

        return self.nodes[node_id]

    def neighbors(self, node_id):

        result = []

        for edge in self.edges:

            if edge.source == node_id:

                result.append(self.nodes[edge.target])

        return result

    def to_dict(self):

        return {

            "nodes": [

                n.to_dict()

                for n in self.nodes.values()

            ],

            "edges": [

                e.to_dict()

                for e in self.edges

            ]

        }