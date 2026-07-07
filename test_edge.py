from igeg.edge import IGEGEdge, EdgeType


edge = IGEGEdge(
    source="Customer",
    target="Customers_Table",
    edge_type=EdgeType.MAPPING,
    weight=0.95,
    metadata={
        "reason": "semantic grounding"
    }
)


print(edge)

print(edge.to_dict())