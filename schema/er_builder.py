import os
import pandas as pd

from schema.entity import Entity


class ERBuilder:

    def __init__(self, data_path):

        self.data_path = data_path

        self.tables = {}

        self.entities = {}

        self.relationships = []

    # --------------------------------------------------

    def load_tables(self):

        print("=" * 60)
        print("Loading CSV files...")
        print("=" * 60)

        for file in os.listdir(self.data_path):

            if file.endswith(".csv"):

                table_name = file.replace(".csv", "")

                full_path = os.path.join(self.data_path, file)

                self.tables[table_name] = pd.read_csv(full_path)

                print(f"Loaded: {table_name}")

        print()
        print(f"Total Tables: {len(self.tables)}")

    # --------------------------------------------------

    def detect_entities(self):

        print()
        print("=" * 60)
        print("Detecting Entities...")
        print("=" * 60)

        self.entities = {}

        for table_name, dataframe in self.tables.items():

            entity = Entity(table_name)

            for column in dataframe.columns:

                entity.add_column(column)

            self.entities[table_name] = entity

            print(f"Entity: {entity.name}")

        print()
        print(f"Total Entities: {len(self.entities)}")

    # --------------------------------------------------

    def print_entities(self):

        print()

        print("=" * 60)
        print("ENTITY DETAILS")
        print("=" * 60)

        for entity in self.entities.values():

            print()

            print(f"Entity : {entity.name}")

            print()

            print("Columns")

            print("-------------")

            for column in entity.columns:

                print(column)