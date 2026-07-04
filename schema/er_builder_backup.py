import pandas as pd

from schema.entity import Entity
from schema.relationship import Relationship
from schema.key_classifier import KeyClassifier


class ERBuilder:

    def __init__(self):

        self.entities = {}

        self.relationships = []

        self.key_classifier = KeyClassifier()

    def build(self, dataframes: dict):

        # ساخت Entity ها
        for name, df in dataframes.items():

            entity = Entity(name)

            self._analyze_columns(entity, df)

            self.entities[name] = entity

        # ساخت روابط
        self._build_relationships()

        return self

    def _analyze_columns(self, entity, df):

        for col in df.columns:

            # 🔥 Primary Key
            if self.key_classifier.is_primary_key(col, df):

                entity.primary_key = col

            # 🔥 Foreign Key واقعی
            elif self._is_real_foreign_key(col, df):

                entity.foreign_keys.append(col)

            # 🔥 External ID (IMDB, TMDB)
            elif self.key_classifier.is_external_id(col):

                entity.attributes.append(col)

            else:

                entity.attributes.append(col)

    def _is_real_foreign_key(self, column, df):

        """
        تشخیص FK واقعی:
        - باید در نام ستون FK-like باشد
        - یا در ارتباط بین DataFrameها استفاده شود
        """

        fk_patterns = ["id", "_id", "key"]

        if any(p == column.lower() for p in fk_patterns):

            return False

        # اگر ستون دقیقا Primary Key یک entity دیگر باشد
        for entity_name, entity in self.entities.items():

            if entity.primary_key == column:

                return True

        return False

    def _build_relationships(self):

        """
        ساخت روابط بین Entity ها بر اساس Foreign Key های واقعی
        """

        for source_name, source_entity in self.entities.items():

            for fk in source_entity.foreign_keys:

                for target_name, target_entity in self.entities.items():

                    if target_entity.primary_key == fk:

                        self.relationships.append(
                            Relationship(
                                source=source_name,
                                target=target_name,
                                source_attr=fk,
                                target_attr=target_entity.primary_key
                            )
                        )

    def get_schema(self):

        return {
            "entities": self.entities,
            "relationships": self.relationships
        }