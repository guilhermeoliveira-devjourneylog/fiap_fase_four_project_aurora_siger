from builders.colony_graph_builder import (
    ColonyGraphBuilder
)

from presenters.graph_printer import (
    GraphPrinter
)

from presenters.rich_graph_printer import (
    RichGraphPrinter
)

from algorithms.dijkstra import (
    DijkstraAlgorithm
)

CENTRO = 0


def reconstruct_path(previous, destination):
    """
    Reconstrói o caminho mínimo a partir do vetor de predecessores.

    A função percorre o vetor `previous`, gerado por um algoritmo de
    caminho mínimo (como Dijkstra), voltando do vértice de destino até
    a origem (quando o valor é None).

    Em seguida, inverte a ordem para retornar o caminho correto
    (origem → destino).

    Parameters
    ----------
    previous : list[int | None]
        Lista onde cada posição representa o predecessor de um vértice
        no caminho mínimo.
    destination : int
        Vértice de destino cujo caminho será reconstruído.

    Returns
    -------
    list[int]
        Lista de vértices representando o caminho da origem até o destino.
    """
    path = []

    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path


def main():
    """
    Executa a simulação completa da colônia baseada em grafos.

    Fluxo principal:
    - Constrói o grafo da colônia
    - Exibe a matriz de adjacência (formato rico e simples)
    - Lista vértices e arestas
    - Executa o algoritmo de Dijkstra a partir do CENTRO
    - Reconstrói e exibe os menores caminhos até todos os nós
    """

    graph = (
        ColonyGraphBuilder()
        .build()
    )

    printer = RichGraphPrinter()
    printer.print_matrix(graph)

    GraphPrinter.print_vertices(graph)
    GraphPrinter.print_edges(graph)

    algorithm = DijkstraAlgorithm()

    result = algorithm.execute(
        graph,
        CENTRO
    )

    print(
        "\nMENORES CAMINHOS "
        "A PARTIR DO CENTRO\n"
    )

    for destination in range(graph.size):

        path = reconstruct_path(
            result.previous,
            destination
        )

        names = [
            graph.vertices[v].name
            for v in path
        ]

        print(
            f"{' → '.join(names):<80}"
            f"{result.distances[destination]} m"
        )


if __name__ == "__main__":
    main()