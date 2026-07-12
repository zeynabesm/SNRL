from igeg.ml.pipeline import MLPipeline



class SNRLRunner:


    def run(
        self,
        X,
        y
    ):


        pipeline = MLPipeline()


        result = pipeline.run(
            X,
            y
        )


        return result