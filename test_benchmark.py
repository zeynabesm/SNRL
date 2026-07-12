from igeg.benchmark.dataset_loader import BenchmarkLoader
from igeg.benchmark.baseline import BaselineModel
from igeg.benchmark.snrl_runner import SNRLRunner
from igeg.benchmark.evaluator import BenchmarkEvaluator



loader = BenchmarkLoader()



# نمونه دیتاست خروجی SNRL
df = loader.load_csv(
    "dataset.csv"
)



X,y = loader.split_target(
    df,
    "Churn"
)



baseline = BaselineModel()



baseline_result = baseline.run(
    X,
    y
)



snrl = SNRLRunner()



snrl_result = snrl.run(
    X,
    y
)



evaluator = BenchmarkEvaluator()



result = evaluator.compare(
    baseline_result,
    snrl_result
)



print("\n=== BENCHMARK RESULT ===")

print(result)