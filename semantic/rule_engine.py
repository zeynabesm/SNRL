class RuleEngine:

    def __init__(self):

        self.rules = []

    def register(self, rule):

        self.rules.append(rule)

    def infer(self, obj):

        for rule in self.rules:

            result = rule.apply(obj)

            if result is not None:

                return result

        return "Unknown"