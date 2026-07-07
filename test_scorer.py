from igeg.scorer import EvidenceScorer



scorer = EvidenceScorer()


path = [

    "Customer",

    "Transactions.amount",

    "AVG",

    "Average Purchase Value",

    "Churn"

]


score = scorer.score(path)


print(
    "Evidence Score:",
    score
)