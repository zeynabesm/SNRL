from intent.intent_parser import IntentParser
from intent.concept_extractor import ConceptExtractor



query = """

Predict customer churn based on purchase behavior

"""


parser = IntentParser()

intent = parser.parse(query)



extractor = ConceptExtractor()


concepts = extractor.extract(intent)



print(intent)

print(concepts)