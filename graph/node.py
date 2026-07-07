class Node:

    """
    Base node representation for SNRL graphs.

    Node types:

    I : Intent
    C : Concept
    T : Table
    A : Attribute
    F : Feature
    O : Operator
    Y : Target
    """

    def __init__(
            self,
            name,
            node_type,
            metadata=None):

        self.name = name

        self.type = node_type

        self.metadata = metadata or {}


    def __repr__(self):

        return (
            f"Node("
            f"name={self.name}, "
            f"type={self.type})"
        )