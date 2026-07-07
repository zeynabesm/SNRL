class SchemaGraph:

    """
    Representation of relational database schema
    for SNRL reasoning engine.

    Schema:
    S = (T, A, R)

    T : Tables
    A : Attributes
    R : Relationships
    """


    def __init__(self):

        self.tables = {}

        self.attributes = {}

        self.relationships = []


    def add_table(self,
                  table_name,
                  columns):

        """
        Add table node

        Example:

        Customers:
            id
            age
            country
        """

        self.tables[table_name] = columns


        for column in columns:

            self.attributes[
                f"{table_name}.{column}"
            ] = {
                "table": table_name,
                "column": column
            }



    def add_relationship(self,
                         table1,
                         column1,
                         table2,
                         column2):

        """
        Add relational edge

        Example:

        Customers.customer_id
                |
                |
        Transactions.customer_id

        """


        relation = {

            "source":
                f"{table1}.{column1}",

            "target":
                f"{table2}.{column2}"

        }


        self.relationships.append(
            relation
        )



    def get_tables(self):

        return list(
            self.tables.keys()
        )



    def get_attributes(self):

        return list(
            self.attributes.keys()
        )



    def show_schema(self):


        print("\n===== TABLES =====")


        for table, columns in self.tables.items():

            print(
                table,
                "->",
                columns
            )


        print("\n===== RELATIONSHIPS =====")


        for r in self.relationships:

            print(
                r["source"],
                "<---->",
                r["target"]
            )