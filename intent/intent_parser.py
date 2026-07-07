class IntentParser:


    """
    Extract structured prediction intent
    from natural language query.

    Output:

    I =
    (
    task,
    target,
    entity,
    constraints
    )

    """


    def __init__(self):

        self.prediction_words = [

            "predict",
            "forecast",
            "estimate"

        ]


        self.classification_targets = [

            "churn",
            "fraud",
            "risk",
            "default"

        ]


        self.entity_keywords = [

            "customer",
            "patient",
            "user",
            "account"

        ]



    def parse(self, query):


        query = query.lower()


        intent = {

            "task": None,

            "target": None,

            "entity": None,

            "constraints": []

        }



        # Task detection

        for word in self.prediction_words:

            if word in query:

                intent["task"] = "prediction"



        # Target detection

        for target in self.classification_targets:

            if target in query:

                intent["target"] = target



        # Entity detection

        for entity in self.entity_keywords:

            if entity in query:

                intent["entity"] = entity



        return intent