from intent.concept_graph import ConceptGraph



class ConceptExtractor:



    def __init__(self):


        self.dictionary = {


            "churn":[

                (
                "customer",
                "purchase"
                ),

                (
                "purchase",
                "transaction"
                ),

                (
                "transaction",
                "activity"
                )

            ]

        }



    def extract_graph(
            self,
            intent):


        graph = ConceptGraph()


        target = intent.get(
            "target"
        )


        relations = self.dictionary.get(
            target,
            []
        )



        created={}



        for a,b in relations:


            if a not in created:

                created[a]=graph.add_concept(a)



            if b not in created:

                created[b]=graph.add_concept(b)



            graph.add_relation(

                created[a],

                created[b],

                "semantic"

            )



        return graph