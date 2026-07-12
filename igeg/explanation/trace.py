class ReasoningTrace:


    def __init__(self):

        self.steps = []



    def add(
        self,
        message
    ):

        self.steps.append(
            message
        )



    def get(self):

        return self.steps