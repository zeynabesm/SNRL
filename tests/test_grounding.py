from schema.schema_graph import SchemaGraph

from grounding.schema_grounder import SchemaGrounder



# Build schema


schema=SchemaGraph()



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
        "amount",
        "date"
    ]

)



# Grounder


grounder=SchemaGrounder(schema)



concepts=[

    "customer",
    "purchase",
    "activity"

]



result=grounder.ground(
    concepts
)



for k,v in result.items():

    print(
        "\n",
        k,
        "=>",
        v
    )