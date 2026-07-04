class ReferenceRule:

    def apply(self, obj):

        if obj.name.lower() in ["links", "lookup", "reference"]:

            return "Reference"

        return None