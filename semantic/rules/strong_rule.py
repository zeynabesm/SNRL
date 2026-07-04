class StrongRule:

    def apply(self, obj):

        if obj.primary_key is not None and len(obj.foreign_keys) == 0:

            return "Strong"

        return None