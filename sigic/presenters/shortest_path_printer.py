from algorithms.dijkstra import reconstruct_path


class ShortestPathPrinter:
    """
    Responsável apenas por exibir caminhos mínimos.
    """

    def __init__(self, graph):
        self.graph = graph

    def print(self, result, source: int):
        """
        Exibe os menores caminhos a partir da origem.
        """

        print("\nMENORES CAMINHOS A PARTIR DO CENTRO\n")

        for destination in range(self.graph.size):

            path = reconstruct_path(
                result.previous,
                destination
            )

            names = [
                self.graph.vertices[v].name
                for v in path
            ]

            print(
                f"{' → '.join(names):<80}"
                f"{result.distances[destination]} m"
            )