class Edge:

    """
    Edge representation in SNRL reasoning graph.

    Edge types:

    semantic
    mapping
    relational
    feature
    inference
    """

    def __init__(
            self,
            source,
            target,
            edge_type,
            weight=0.0):


        self.source = source

        self.target = target

        self.type = edge_type

        self.weight = weight



    def __repr__(self):

        return (
            f"Edge("
            f"{self.source.name}"
            f" --{self.type}--> "
            f"{self.target.name})"
        )