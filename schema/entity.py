class Entity:

    def __init__(self, name):

        self.name = name

        self.columns = []

        self.primary_key = None

        self.foreign_keys = []

        self.attributes = []

    def add_column(self, column):

        self.columns.append(column)

    def __str__(self):

        return self.name