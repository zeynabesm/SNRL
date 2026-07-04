class SchemaGraph:

    def __init__(self):

        self.entities = {}

        self.relationships = []

    def add_entity(self, entity):

        self.entities[entity.name] = entity

    def add_relationship(self, relationship):

        self.relationships.append(relationship)

    def print_graph(self):

        print("=" * 60)
        print("ER SCHEMA GRAPH")
        print("=" * 60)

        print("\nEntities")

        for entity in self.entities.values():
            print(f"- {entity.name}")

        print("\nRelationships")

        for rel in self.relationships:
            print(f"{rel.source} --{rel.key}--> {rel.target}")