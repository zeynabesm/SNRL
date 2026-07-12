from sklearn.metrics import accuracy_score



class MLEvaluator:


    def evaluate(
        self,
        model,
        X_test,
        y_test
    ):


        prediction = model.predict(
            X_test
        )


        score = accuracy_score(
            y_test,
            prediction
        )


        return {

            "accuracy": score,

            "predictions": prediction.tolist()

        }