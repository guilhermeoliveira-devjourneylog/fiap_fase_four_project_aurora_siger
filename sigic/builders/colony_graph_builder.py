from models.graph import Graph
from models.vertex import Vertex
from models.edge import Edge


class ColonyGraphBuilder:
    """
    Construtor do grafo que modela a infraestrutura da colônia.

    Esta classe é responsável por criar e inicializar um grafo completo
    representando os módulos da colônia (controle, energia, agricultura, etc.)
    e suas conexões com pesos associados.
    """

    def build(self) -> Graph:
        """
        Constrói e retorna o grafo completo da colônia.

        Returns:
            Graph: Grafo inicializado com vértices e arestas da colônia.
        """
        graph = Graph(9)

        self._add_vertices(graph)
        self._add_edges(graph)

        return graph

    def _add_vertices(self, graph: Graph) -> None:
        """
        Adiciona os vértices que representam os módulos da colônia ao grafo.

        Cada vértice representa uma unidade funcional da infraestrutura,
        como Centro de Controle, Agricultura, Energia, entre outros.

        Args:
            graph (Graph): Grafo onde os vértices serão inseridos.
        """
        vertices = {
            0: "Centro de Controle",
            1: "Agricultura",
            2: "Comunicacao",
            3: "Pesquisa",
            4: "Recursos",
            5: "Energia",
            6: "Medico",
            7: "Habitacao",
            8: "Transporte",
        }

        for idx, name in vertices.items():
            graph.add_vertex(
                Vertex(idx, name)
            )

    def _add_edges(self, graph: Graph) -> None:
        """
        Adiciona as arestas ponderadas que representam as conexões
        entre os módulos da colônia.

        Cada aresta possui um peso que pode representar custo energético,
        distância ou prioridade de comunicação entre os módulos.

        Args:
            graph (Graph): Grafo onde as arestas serão inseridas.
        """
        edges = [
            (0, 1, 250),
            (0, 2, 180),
            (0, 3, 220),
            (0, 4, 260),
            (0, 5, 120),
            (0, 6, 200),
            (0, 7, 170),
            (0, 8, 300),

            (5, 1, 140),
            (5, 2, 150),
            (5, 3, 160),
            (5, 4, 190),
            (5, 6, 170),
            (5, 7, 130),
            (5, 8, 210),

            (1, 2, 110),
            (1, 4, 90),

            (2, 3, 130),

            (3, 4, 80),

            (6, 7, 95),

            (7, 8, 145),

            (4, 8, 175),
        ]

        for source, target, distance in edges:
            graph.add_edge(
                Edge(source, target, distance)
            )