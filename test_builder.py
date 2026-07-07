from igeg.builder import IGEGBuilder
from igeg.edge import EdgeType



builder = IGEGBuilder()



intent = builder.add_intent(
    {
        "name":"Predict Customer Churn",
        "task":"classification",
        "target":"churn",
        "entity":"customer"
    }
)



customer = builder.add_concept(
    "Customer"
)



customers_table = builder.add_table(
    "Customers"
)



builder.connect(
    intent,
    customer,
    EdgeType.SEMANTIC,
    weight=0.9,
    metadata={
        "reason":"intent understanding"
    }
)



builder.connect(
    customer,
    customers_table,
    EdgeType.MAPPING,
    weight=0.95,
    metadata={
        "reason":"schema grounding"
    }
)



graph = builder.build()



graph.print_graph()



print(graph.to_dict())