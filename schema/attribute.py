class Attribute:

    def __init__(self, name, dtype):
        self.name = name
        self.dtype = dtype

    def __repr__(self):
        return f"{self.name} ({self.dtype})"