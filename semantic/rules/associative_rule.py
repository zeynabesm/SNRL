class AssociativeRule:

    def apply(self, obj):

        if obj.primary_key is None and len(obj.foreign_keys) >= 2:

            return "Associative"

        return None