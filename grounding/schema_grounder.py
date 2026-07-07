from difflib import SequenceMatcher



class SchemaGrounder:
    """
    Evidence-based Concept to Schema Grounding

    Maps:

        Concept -> Schema Element

    using:

        1. Semantic similarity
        2. Schema metadata evidence


    Future extension:

        + Relation evidence
        + Data statistics
        + Embedding similarity

    """


    def __init__(
            self,
            schema_graph,
            metadata):

        self.schema = schema_graph

        self.metadata = metadata



    # ---------------------------------
    # Semantic similarity
    # ---------------------------------

    def semantic_score(
            self,
            concept,
            attribute):


        return SequenceMatcher(

            None,

            concept.lower(),

            attribute.lower()

        ).ratio()



    # ---------------------------------
    # Metadata evidence score
    # ---------------------------------

    def metadata_score(
            self,
            concept,
            column):


        info = self.metadata.get_column(column)


        if info is None:

            return 0



        score = 0



        for tag in info.tags:


            if concept.lower() == tag.lower():

                score += 1



        if score > 0:

            return 1



        return 0



    # ---------------------------------
    # Combined Evidence Score
    # ---------------------------------

    def evidence_score(
            self,
            concept,
            column):


        semantic = self.semantic_score(

            concept,

            column.split(".")[-1]

        )


        metadata = self.metadata_score(

            concept,

            column

        )


        final_score = (

            0.4 * semantic

            +

            0.6 * metadata

        )


        return final_score



    # ---------------------------------
    # Find best schema candidates
    # ---------------------------------

    def find_best_match(
            self,
            concept):


        candidates = []



        for column, info in self.metadata.all_columns():


            score = self.evidence_score(

                concept,

                column

            )


            candidates.append(

                (
                    column,

                    score

                )

            )



        candidates.sort(

            key=lambda x:x[1],

            reverse=True

        )


        return candidates[:3]



    # ---------------------------------
    # Ground all concepts
    # ---------------------------------

    def ground(
            self,
            concepts):


        mappings = {}



        for concept in concepts:


            mappings[concept] = self.find_best_match(

                concept

            )



        return mappings