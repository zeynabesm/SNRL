from collections import deque


class EvidencePathSearcher:

    def __init__(self, graph, scorer):

        self.graph = graph
        self.scorer = scorer


    def get_node_object(self, node):

        """
        Convert node id to IGEGNode object
        """

        # already object
        if hasattr(node, "name"):
            return node


        # search in graph nodes

        if isinstance(self.graph.nodes, dict):

            return self.graph.nodes.get(node)


        for n in self.graph.nodes:

            if hasattr(n, "id") and n.id == node:
                return n


        return None



    def get_neighbors(self, node):

        """
        Return neighbor node objects
        """

        neighbors = []


        node_id = node.id


        for edge in self.graph.edges:


            if edge.source == node_id:


                target = self.get_node_object(
                    edge.target
                )


                if target:
                    neighbors.append(target)



        return neighbors



    def find_paths(
        self,
        start_node,
        target_type="target",
        max_depth=8
    ):


        paths = []


        queue = deque()


        queue.append(
            [start_node]
        )


        while queue:


            current_path = queue.popleft()


            current_node = current_path[-1]



            if current_node.node_type.value == target_type:

                paths.append(
                    current_path
                )

                continue



            if len(current_path) >= max_depth:

                continue



            neighbors = self.get_neighbors(
                current_node
            )



            for neighbor in neighbors:


                if neighbor not in current_path:


                    queue.append(
                        current_path + [neighbor]
                    )


        return paths



    def rank_paths(
        self,
        paths
    ):


        results = []



        for path in paths:


            names = [

                node.name

                for node in path

            ]


            score = self.scorer.score(
                names
            )


            results.append(
                {
                    "path": names,
                    "score": score
                }
            )



        return sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )