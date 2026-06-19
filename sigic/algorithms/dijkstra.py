from dataclasses import dataclass
from algorithms.shortest_path import ShortestPathAlgorithm


@dataclass
class ShortestPathResult:
    """
    Estrutura de retorno do algoritmo de menor caminho.

    Attributes:
        distances (list): Distância mínima de cada vértice a partir da origem.
        previous (list): Vetor de predecessores para reconstrução do caminho.
    """
    distances: list
    previous: list


class DijkstraAlgorithm(ShortestPathAlgorithm):
    """
    Implementação do algoritmo de Dijkstra para cálculo de caminhos mínimos
    em um grafo com pesos não negativos.

    O algoritmo utiliza uma abordagem gulosa sem fila de prioridade,
    selecionando iterativamente o vértice não visitado com menor distância
    conhecida.
    """

    def execute(self, graph, source) -> ShortestPathResult:
        """
        Executa o algoritmo de Dijkstra a partir de um vértice de origem.

        Args:
            graph: Grafo contendo os vértices e a função neighbors().
            source (int): Vértice de origem.

        Returns:
            ShortestPathResult: Estrutura contendo:
                - distances: menor distância do source até cada vértice
                - previous: vetor de predecessores para reconstrução do caminho
        """
        distances = [float("inf")] * graph.size
        distances[source] = 0

        previous = [None] * graph.size
        visited = [False] * graph.size

        for _ in range(graph.size):

            current = None
            min_distance = float("inf")

            for vertex in range(graph.size):
                if not visited[vertex] and distances[vertex] < min_distance:
                    current = vertex
                    min_distance = distances[vertex]

            if current is None:
                break

            visited[current] = True

            for neighbor, distance in graph.neighbors(current):

                if visited[neighbor]:
                    continue

                alternative = distances[current] + distance

                if alternative < distances[neighbor]:
                    distances[neighbor] = alternative
                    previous[neighbor] = current

        return ShortestPathResult(
            distances=distances,
            previous=previous
        )