from models.vertex import Vertex
from models.edge import Edge


class Graph:
    """
    Estrutura de armazenamento de um grafo baseado em matriz de adjacência.

    Esta classe representa um grafo ponderado, podendo ser direcionado ou não,
    onde os vértices são armazenados em um dicionário e as arestas são representadas
    por uma matriz de adjacência.

    A matriz adjacente (adj_matrix) armazena o peso (distância) entre dois vértices.
    Caso não exista conexão entre dois nós, o valor é None.

    Características principais:
    - Não implementa algoritmos de busca ou roteamento (ex: Dijkstra, BFS, DFS).
    - Não contém lógica de apresentação ou visualização.
    - Responsável exclusivamente pelo armazenamento e manipulação estrutural do grafo.
    """

    def __init__(self, size: int):
        """
        Inicializa a estrutura do grafo.

        Args:
            size (int): Número total de vértices suportados pelo grafo.

        Estrutura criada:
        - vertices: dicionário que mapeia id -> Vertex
        - adj_matrix: matriz quadrada size x size com valores None ou pesos
        """
        self.size = size
        self.vertices: dict[int, Vertex] = {}

        self.adj_matrix = [
            [None] * size
            for _ in range(size)
        ]

    def add_vertex(self, vertex: Vertex) -> None:
        """
        Adiciona um vértice ao grafo.

        Args:
            vertex (Vertex): Objeto que representa um nó do grafo.

        Observação:
        O vértice é armazenado pelo seu identificador (vertex.id).
        """
        self.vertices[vertex.id] = vertex

    def add_edge(self, edge: Edge) -> None:
        """
        Adiciona uma aresta ponderada entre dois vértices.

        Args:
            edge (Edge): Objeto contendo origem, destino e distância/peso.

        Observação:
        A implementação atual assume grafo não direcionado,
        pois registra a conexão nos dois sentidos.
        """
        self.adj_matrix[edge.source][edge.target] = edge.distance
        self.adj_matrix[edge.target][edge.source] = edge.distance

    def get_distance(self, u: int, v: int):
        """
        Retorna o peso (distância) entre dois vértices.

        Args:
            u (int): vértice de origem
            v (int): vértice de destino

        Returns:
            valor numérico da distância ou None caso não exista aresta
        """
        return self.adj_matrix[u][v]

    def neighbors(self, vertex: int):
        """
        Retorna os vizinhos de um vértice.

        Args:
            vertex (int): índice do vértice

        Yields:
            tuple[int, int]: (vizinho, distância)

        Observação:
        Percorre a linha correspondente na matriz de adjacência,
        retornando apenas conexões existentes (não-None).
        """
        for neighbor in range(self.size):
            distance = self.adj_matrix[vertex][neighbor]

            if distance is not None:
                yield neighbor, distance