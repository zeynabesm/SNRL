from intent.intent_parser import IntentParser
from intent.concept_extractor import ConceptExtractor



query="Predict customer churn"


parser=IntentParser()

intent=parser.parse(query)



extractor=ConceptExtractor()


cg=extractor.extract_graph(intent)


cg.show()