class BenchmarkEvaluator:


    def compare(
        self,
        baseline,
        snrl
    ):


        return {

            "baseline_accuracy":
            baseline["accuracy"],


            "snrl_accuracy":
            snrl["evaluation"]["accuracy"],


            "improvement":
            snrl["evaluation"]["accuracy"]
            -
            baseline["accuracy"]

        }