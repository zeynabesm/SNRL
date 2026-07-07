from intent.intent_parser import IntentParser



parser = IntentParser()



query = """
Predict customer churn based on purchase behavior
"""


intent = parser.parse(query)



print(intent)