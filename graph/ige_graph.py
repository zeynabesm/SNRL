from graph.node import Node
from graph.edge import Edge



class IGEG:

    """
    Intent-Grounded Evidence Graph

    Core representation of SNRL.

    Nodes:
        Intent
        Concept
        Table
        Attribute
        Feature
        Operator
        Target

    Edges:
        semantic
        mapping
        relational
        feature
        inference
    """



    def __init__(self):

        # V
        self.nodes = []


        # E
        self.edges = []



    # -------------------------
    # Node Operations
    # -------------------------


    def add_node(
            self,
            node):

        """
        Add node to graph
        """

        if node not in self.nodes:

            self.nodes.append(node)



    def create_node(
            self,
            name,
            node_type,
            metadata=None):

        """
        Helper function
        """

        node = Node(
            name,
            node_type,
            metadata
        )


        self.add_node(node)


        return node



    # -------------------------
    # Edge Operations
    # -------------------------


    def add_edge(
            self,
            source,
            target,
            edge_type,
            weight=0.0):


        """
        Add reasoning relationship
        """

        edge = Edge(
            source,
            target,
            edge_type,
            weight
        )


        self.edges.append(edge)


        return edge



    # -------------------------
    # Search
    # -------------------------


    def get_nodes_by_type(
            self,
            node_type):

        """
        Retrieve nodes of specific type

        Example:

        get_nodes_by_type("T")

        returns tables
        """

        return [

            node

            for node in self.nodes

            if node.type == node_type

        ]



    def neighbors(
            self,
            node):

        """
        Find connected nodes
        """

        result=[]


        for edge in self.edges:


            if edge.source == node:

                result.append(
                    edge.target
                )


            elif edge.target == node:

                result.append(
                    edge.source
                )


        return result



    # -------------------------
    # Graph Summary
    # -------------------------


    def summary(self):


        print("\n===== IGEG NODES =====")


        for node in self.nodes:

            print(node)



        print(
            "\n===== IGEG EDGES ====="
        )


        for edge in self.edges:

            print(edge)