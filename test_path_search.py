from igeg.path_search import EvidencePathSearcher
from igeg.scorer import EvidenceScorer
from igeg.builder import IGEGBuilder
from igeg.node import IGEGNode, NodeType



# ----------------------------
# Create IGEG Builder
# ----------------------------

builder = IGEGBuilder()



# ----------------------------
# Create Intent Node
# ----------------------------

intent = IGEGNode(
    node_type=NodeType.INTENT,
    name="Predict Customer Churn"
)


builder.add_node(intent)



# ----------------------------
# Add schema grounding
# ----------------------------

builder.build_from_grounding(

    "Predict Customer Churn",

    {

        "Customer":
        {
            "table": "Customers",
            "attribute": "customer_id"
        },


        "Purchase":
        {
            "table": "Transactions",
            "attribute": "amount"
        }

    }

)



# ----------------------------
# Build Graph
# ----------------------------

graph = builder.build()



# ----------------------------
# Print graph structure
# ----------------------------

print("\n===== GRAPH =====")


print("Nodes:")

for key, value in graph.nodes.items():

    print(
        key,
        "=>",
        value.name,
        value.node_type
    )



print("\nEdges:")

for edge in graph.edges:

    print(
        edge.source,
        "->",
        edge.target,
        edge.edge_type
    )



# ----------------------------
# Evidence Search
# ----------------------------

scorer = EvidenceScorer()


searcher = EvidencePathSearcher(
    graph,
    scorer
)



paths = searcher.find_paths(
    intent
)



print("\n===== PATHS =====")


if not paths:

    print(
        "No evidence path found"
    )


else:

    ranked = searcher.rank_paths(
        paths
    )


    for item in ranked:

        print(item)