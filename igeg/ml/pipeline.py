from igeg.ml.trainer import MLTrainer
from igeg.ml.evaluator import MLEvaluator

from igeg.explanation.trace import ReasoningTrace
from igeg.explanation.attribution import FeatureAttributor



class MLPipeline:



    def __init__(self):

        self.trainer = MLTrainer()

        self.evaluator = MLEvaluator()

        self.attributor = FeatureAttributor()



    def run(
        self,
        X,
        y,
        evidence_path=None
    ):


        trace = ReasoningTrace()



        trace.add(
            "Dataset generated from SNRL reasoning"
        )



        if evidence_path:

            trace.add(
                "Evidence Path: "
                +
                " -> ".join(
                    node.name
                    for node in evidence_path.nodes
                )
            )



        result = self.trainer.train(
            X,
            y
        )



        evaluation = self.evaluator.evaluate(
            result["model"],
            result["X_test"],
            result["y_test"]
        )



        attribution = self.attributor.explain(
            result["model"],
            X.columns
        )



        return {

            "evaluation": evaluation,

            "feature_attribution": attribution,

            "reasoning_trace": trace.get()

        }