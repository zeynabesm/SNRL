class SemanticObject:

    def __init__(self, name):

        self.name = name

        # Structural Type
        self.entity_type = ""

        # Semantic Role (NEW IDEA)
        self.semantic_role = ""

        self.primary_key = None

        self.attributes = []

        self.foreign_keys = []

        self.in_relations = []

        self.out_relations = []

        self.neighbors = []

        self.degree = 0

        self.statistics = {}

        self.embedding = None

    def __str__(self):

        text = []

        text.append("=" * 60)
        text.append(f"Entity : {self.name}")

        text.append(f"Type   : {self.entity_type}")
        text.append(f"Role   : {self.semantic_role}")

        text.append(f"Primary Key : {self.primary_key}")

        text.append(f"Foreign Keys : {self.foreign_keys}")

        text.append(f"Attributes : {self.attributes}")

        text.append(f"Neighbors : {self.neighbors}")

        text.append(f"Degree : {self.degree}")

        return "\n".join(text)