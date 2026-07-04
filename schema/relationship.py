class Relationship:

    def __init__(self, source, target, key):

        self.source = source
        self.target = target
        self.key = key

    def __repr__(self):
        return f"{self.source} --{self.key}--> {self.target}"