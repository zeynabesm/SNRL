from igeg.node import IGEGNode, NodeType

nodes = [
    IGEGNode(NodeType.INTENT, "Predict Customer Churn"),
    IGEGNode(NodeType.CONCEPT, "Customer"),
    IGEGNode(NodeType.TABLE, "Customers"),
    IGEGNode(NodeType.ATTRIBUTE, "customer_id"),
    IGEGNode(NodeType.OPERATOR, "AVG"),
    IGEGNode(NodeType.FEATURE, "Average Purchase"),
    IGEGNode(NodeType.TARGET, "Churn")
]

for node in nodes:
    print(node.to_dict())
   
intent = IGEGNode(
    node_type=NodeType.INTENT,
    name="Predict Customer Churn",
    metadata={
        "task": "classification",
        "entity": "customer",
        "target": "churn"
    }
)

print(intent.to_dict())