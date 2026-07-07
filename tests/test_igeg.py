from graph.ige_graph import IGEG



graph = IGEG()



# Intent Node

intent = graph.create_node(
    "Predict Customer Churn",
    "I"
)



# Concept Node

customer = graph.create_node(
    "Customer",
    "C"
)



# Table Node

customers_table = graph.create_node(
    "Customers",
    "T"
)



transactions_table = graph.create_node(
    "Transactions",
    "T"
)



# Feature Node

avg_purchase = graph.create_node(
    "Average Purchase Value",
    "F"
)



# Edges

graph.add_edge(
    intent,
    customer,
    "semantic",
    0.9
)


graph.add_edge(
    customer,
    customers_table,
    "mapping",
    0.8
)


graph.add_edge(
    customers_table,
    transactions_table,
    "relational",
    0.95
)


graph.add_edge(
    transactions_table,
    avg_purchase,
    "feature",
    0.7
)



graph.summary()