class FeatureAttributor:


    def explain(
        self,
        model,
        features
    ):


        importance = model.feature_importances_


        result = {}


        for name,value in zip(
            features,
            importance
        ):

            result[name] = float(value)


        return result