class RoleEngine:

    def infer(self, obj):

        # 1. CORE ENTITY (بالاترین اولویت)
        if obj.entity_type == "Strong" and obj.degree >= 2:

            return "Core Entity"

        # 2. BRIDGE ENTITY
        if obj.entity_type in ["Associative", "Reference"]:

            if obj.degree >= 2:

                return "Bridge Entity"

        # 3. INTERACTION ENTITY
        if obj.entity_type == "Associative":

            return "Interaction Entity"

        # 4. LEAF ENTITY (آخرین گزینه)
        if obj.degree <= 1:

            return "Leaf Entity"

        return "Unknown"