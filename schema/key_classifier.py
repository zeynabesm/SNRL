class KeyClassifier:

    def is_primary_key(self, column, df):

        return column == "id" or column.endswith("Id") and df[column].is_unique


    def is_foreign_key(self, column, graph):

        # اگر در Graph به Entity دیگر وصل کند
        for rel in graph.relationships:

            if rel.source_attr == column or rel.target_attr == column:

                return True

        return False


    def is_external_id(self, column):

        external_patterns = ["imdb", "tmdb", "uuid", "external"]

        return any(p in column.lower() for p in external_patterns)