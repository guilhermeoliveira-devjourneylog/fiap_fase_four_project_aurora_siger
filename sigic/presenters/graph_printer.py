class GraphPrinter:
    """
    Responsável por exibir, em formato textual, os vértices e as arestas
    de um grafo.

    Esta classe atua apenas na apresentação dos dados, separando a lógica
    de visualização da estrutura do grafo e dos algoritmos aplicados sobre ele.
    """

    @staticmethod
    def print_vertices(graph):
        """
        Exibe todos os vértices cadastrados no grafo.

        Args:
            graph (Graph): Grafo contendo os vértices a serem exibidos.
        """

        print("\nVÉRTICES\n")

        for vertex in graph.vertices.values():

            print(
                f"{vertex.id}: "
                f"{vertex.name}"
            )

    @staticmethod
    def print_edges(graph):
        """
        Exibe todas as arestas do grafo e suas respectivas distâncias.

        Percorre a matriz de adjacência considerando apenas a metade superior
        da matriz para evitar a exibição duplicada de conexões em grafos não
        direcionados. Ao final, apresenta a quantidade total de arestas.

        Args:
            graph (Graph): Grafo contendo as conexões a serem exibidas.
        """

        print("\nARESTAS\n")

        total = 0

        for i in range(graph.size):

            for j in range(i + 1, graph.size):

                distance = graph.get_distance(
                    i,
                    j
                )

                if distance is not None:

                    print(
                        f"{graph.vertices[i].name}"
                        f" ↔ "
                        f"{graph.vertices[j].name}"
                        f" ({distance} m)"
                    )

                    total += 1

        print(f"\nTOTAL: {total}")