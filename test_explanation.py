from igeg.execution.database import SQLiteDatabase
from igeg.execution.executor import DatasetExecutor

from igeg.ml.pipeline import MLPipeline



db = SQLiteDatabase(
    "snrl.db"
)


executor = DatasetExecutor(
    db
)



sql = """

SELECT
    c.customer_id,
    AVG(t.amount) AS AveragePurchaseValue,
    c.Churn

FROM Customers c

JOIN Transactions t

ON c.customer_id=t.customer_id

GROUP BY c.customer_id;

"""



dataset = executor.run(sql)



X,y = executor.split_target(
    dataset,
    "Churn"
)



pipeline = MLPipeline()



result = pipeline.run(
    X,
    y
)



print("\n=== EVALUATION ===")

print(
    result["evaluation"]
)



print("\n=== FEATURE ATTRIBUTION ===")

print(
    result["feature_attribution"]
)



print("\n=== REASONING TRACE ===")

for step in result["reasoning_trace"]:

    print(step)