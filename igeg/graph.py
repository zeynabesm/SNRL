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


    def get_node(self, node_id: str):

        return self.nodes.get(node_id)


    def get_neighbors(self, node_id: str):

        neighbors = []

        for edge in self.edges:

            if edge.source == node_id:

                target_node = self.nodes.get(edge.target)

                if target_node:
                    neighbors.append(target_node)

        return neighbors


    def to_dict(self):

        return {

            "nodes": [

                node.to_dict()

                for node in self.nodes.values()

            ],

            "edges": [

                edge.to_dict()

                for edge in self.edges

            ]

        }


    def print_graph(self):

        for edge in self.edges:

            source = self.nodes.get(edge.source)

            target = self.nodes.get(edge.target)


            if source and target:

                print(
                    f"{source.name} "
                    f"--[{edge.edge_type.value}]--> "
                    f"{target.name}"
                )