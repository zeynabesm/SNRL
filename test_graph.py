from igeg.graph import IGEGGraph

from igeg.node import IGEGNode, NodeType

from igeg.edge import IGEGEdge, EdgeType



# Create graph

graph = IGEGGraph()



# Create nodes

intent = IGEGNode(
    NodeType.INTENT,
    "Predict Customer Churn",
    metadata={
        "task": "classification",
        "target": "churn",
        "entity": "customer"
    }
)


concept = IGEGNode(
    NodeType.CONCEPT,
    "Customer"
)


table = IGEGNode(
    NodeType.TABLE,
    "Customers"
)



# Add nodes

graph.add_node(intent)

graph.add_node(concept)

graph.add_node(table)



# Create edges

semantic_edge = IGEGEdge(
    source=intent.id,
    target=concept.id,
    edge_type=EdgeType.SEMANTIC,
    weight=0.9,
    metadata={
        "reason": "intent concept relation"
    }
)



mapping_edge = IGEGEdge(
    source=concept.id,
    target=table.id,
    edge_type=EdgeType.MAPPING,
    weight=0.95,
    metadata={
        "reason": "schema grounding"
    }
)



# Add edges

graph.add_edge(semantic_edge)

graph.add_edge(mapping_edge)



# Print graph path

print("\n=== IGEG Reasoning Path ===")

graph.print_graph()



# Print JSON structure

print("\n=== IGEG JSON ===")

print(graph.to_dict())