from schema.schema_graph import SchemaGraph



schema = SchemaGraph()



schema.add_table(
    "Customers",
    [
        "customer_id",
        "age",
        "country"
    ]
)



schema.add_table(
    "Transactions",
    [
        "transaction_id",
        "customer_id",
        "amount"
    ]
)



schema.add_relationship(
    "Customers",
    "customer_id",
    "Transactions",
    "customer_id"
)



schema.show_schema()