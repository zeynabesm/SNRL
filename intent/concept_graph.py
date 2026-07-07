from graph.node import Node
from graph.edge import Edge



class ConceptGraph:


    """
    Semantic Concept Graph

    CG=(Vc,Ec)


    Nodes:
        concepts


    Edges:
        semantic relations

    """



    def __init__(self):

        self.nodes = []

        self.edges = []



    def add_concept(
            self,
            name):


        node = Node(
            name,
            "C"
        )


        self.nodes.append(node)


        return node



    def add_relation(
            self,
            source,
            target,
            relation):


        edge = Edge(

            source,

            target,

            relation

        )


        self.edges.append(edge)



    def get_node(
            self,
            name):


        for node in self.nodes:

            if node.name == name:

                return node


        return None



    def show(self):


        print("\n===== CONCEPT NODES =====")


        for node in self.nodes:

            print(node)



        print(
            "\n===== CONCEPT RELATIONS ====="
        )


        for edge in self.edges:

            print(edge)