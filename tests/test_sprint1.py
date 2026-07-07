from schema.schema_graph import SchemaGraph

from intent.intent_parser import IntentParser

from intent.concept_extractor import ConceptExtractor

from grounding.schema_grounder import SchemaGrounder

from schema.schema_metadata import SchemaMetadata

print("\n==============================")
print(" SNRL Sprint 1 Integration Test")
print("==============================\n")



# --------------------------------
# 1. Build Database Schema
# --------------------------------


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
        "amount",
        "date"
    ]
)



schema.add_relationship(

    "Customers",

    "customer_id",

    "Transactions",

    "customer_id"

)

# --------------------------------
# 1.5 Schema Metadata
# --------------------------------

metadata = SchemaMetadata()


metadata.add_column(
    "Transactions",
    "amount",
    "numeric",
    [
        "purchase",
        "payment",
        "value",
        "transaction"
    ]
)


metadata.add_column(
    "Transactions",
    "amount",
    "numeric",
    [
        "purchase",
        "payment",
        "value",
        "transaction"
    ],
    "measure"

)


metadata.add_column(
    "Transactions",
    "date",
    "datetime",
    [
        "time",
        "activity",
        "recency"
    ],
    "timestamp"
)



metadata.add_column(
    "Transactions",
    "customer_id",
    "id",
    [
        "customer",
        "user",
        "entity"
    ],
    "foreign_key"
)



metadata.add_column(
    "Transactions",
    "transaction_id",
    "id",
    [
        "transaction",
        "entity"
    ],
    "identifier"
)


print("\nSTEP 1.5: Schema Metadata")


for col, info in metadata.all_columns():

    print(
        col,
        "=>",
        info
    )

print("STEP 1: Schema Created")

schema.show_schema()



# --------------------------------
# 2. User Query
# --------------------------------


query = """

Predict customer churn based on purchase behavior

"""


print("\nSTEP 2: User Query")

print(query)



# --------------------------------
# 3. Intent Parsing
# --------------------------------


parser = IntentParser()


intent = parser.parse(query)



print("\nSTEP 3: Intent")

print(intent)



# --------------------------------
# 4. Concept Extraction
# --------------------------------

# --------------------------------
# 4. Concept Graph Extraction
# --------------------------------


extractor = ConceptExtractor()


concept_graph = extractor.extract_graph(intent)



print("\nSTEP 4: Concept Graph")


concept_graph.show()
# --------------------------------
# 5. Schema Grounding
# --------------------------------


concept_names = [

    node.name

    for node in concept_graph.nodes

]


grounder = SchemaGrounder(
    schema,
    metadata
)


mapping = grounder.ground(
    concept_names
)



print("\nSTEP 5: Schema Grounding")


for concept, matches in mapping.items():

    print("\nConcept:", concept)

    for match in matches:

        print(
            "   ",
            match
        )