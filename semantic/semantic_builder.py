from semantic.semantic_object import SemanticObject
from semantic.role_engine import RoleEngine

from semantic.rule_engine import RuleEngine

from semantic.rules.strong_rule import StrongRule
from semantic.rules.weak_rule import WeakRule
from semantic.rules.associative_rule import AssociativeRule
from semantic.rules.reference_rule import ReferenceRule


class SemanticBuilder:

    def __init__(self, graph):

        self.graph = graph

        self.semantic_objects = {}

    # =========================================================

    def build(self):

        self.create_semantic_objects()

        self.detect_types()

        self.compute_degree()

        self.compute_neighbors()

        self.detect_roles()

    # =========================================================

    def create_semantic_objects(self):

        for entity in self.graph.entities.values():

            obj = SemanticObject(entity.name)

            obj.primary_key = entity.primary_key

            obj.foreign_keys = entity.foreign_keys.copy()

            obj.attributes = [

                att.name

                for att in entity.attributes

                if att.name != entity.primary_key
                and att.name not in entity.foreign_keys

            ]

            self.semantic_objects[obj.name] = obj

    # =========================================================

    def detect_types(self):

        engine = RuleEngine()

        engine.register(StrongRule())
        engine.register(AssociativeRule())
        engine.register(WeakRule())
        engine.register(ReferenceRule())

        for obj in self.semantic_objects.values():

            obj.entity_type = engine.infer(obj)

    # =========================================================

    def compute_degree(self):

        for obj in self.semantic_objects.values():

            obj.degree = 0

        for rel in self.graph.relationships:

            self.semantic_objects[rel.source].degree += 1

            self.semantic_objects[rel.target].degree += 1

    # =========================================================

    def compute_neighbors(self):

        for obj in self.semantic_objects.values():

            obj.neighbors = []

        for rel in self.graph.relationships:

            self.semantic_objects[rel.source].neighbors.append(rel.target)

            self.semantic_objects[rel.target].neighbors.append(rel.source)

    # =========================================================

    def detect_roles(self):

        engine = RoleEngine()

        for obj in self.semantic_objects.values():

            obj.semantic_role = engine.infer(obj)

    # =========================================================

    def print_objects(self):

        print()

        print("=" * 70)

        print("SEMANTIC OBJECTS")

        print("=" * 70)

        for obj in self.semantic_objects.values():

            print("=" * 60)

            print(f"Entity : {obj.name}")

            print(f"Type   : {obj.entity_type}")

            print(f"Role   : {obj.semantic_role}")

            print(f"Primary Key : {obj.primary_key}")

            print(f"Foreign Keys : {obj.foreign_keys}")

            print(f"Attributes : {obj.attributes}")

            print(f"Neighbors : {obj.neighbors}")

            print(f"Degree : {obj.degree}")

            print()