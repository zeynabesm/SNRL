class ColumnMetadata:


    def __init__(
            self,
            name,
            data_type,
            tags=None,
            role=None):

        self.name = name

        self.data_type = data_type

        self.tags = tags or []

        # New Evidence Layer
        # Examples:
        # identifier
        # foreign_key
        # measure
        # timestamp
        # categorical

        self.role = role



    def __repr__(self):

        return (
            f"{self.name}"
            f" | type={self.data_type}"
            f" | role={self.role}"
            f" | tags={self.tags}"
        )





class SchemaMetadata:


    def __init__(self):

        self.columns = {}



    def add_column(
            self,
            table,
            column,
            data_type,
            tags=None,
            role=None):


        key = f"{table}.{column}"


        self.columns[key] = ColumnMetadata(

            column,

            data_type,

            tags,

            role

        )



    def get_column(
            self,
            key):

        return self.columns.get(key)



    def all_columns(self):

        return self.columns.items()