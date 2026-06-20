from builders.colony_graph_builder import (
    ColonyGraphBuilder
)

from presenters.graph_printer import (
    GraphPrinter
)

from presenters.rich_graph_printer import (
    RichGraphPrinter
)

from presenters.energy_printer import (
    EnergyPrinter
)

from algorithms.dijkstra import (
    DijkstraAlgorithm
)

from algorithms.energy_growth import (
    EnergyGrowth
)

CENTRO = 0


def reconstruct_path(
    previous,
    destination
):
    """
    Reconstrói o caminho mínimo a partir
    do vetor de predecessores.

    Parameters
    ----------
    previous : list[int | None]
        Vetor de predecessores.

    destination : int
        Destino do caminho.

    Returns
    -------
    list[int]
        Caminho origem → destino.
    """

    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    path.reverse()

    return path


def print_shortest_paths(
    graph,
    source
):
    """
    Exibe os menores caminhos
    a partir do vértice origem.
    """

    algorithm = DijkstraAlgorithm()

    result = algorithm.execute(
        graph,
        source
    )

    print(
        "\nMENORES CAMINHOS "
        "A PARTIR DO CENTRO\n"
    )

    for destination in range(
        graph.size
    ):

        path = reconstruct_path(
            result.previous,
            destination
        )

        names = [

            graph
            .vertices[v]
            .name

            for v in path
        ]

        print(
            f"{' → '.join(names):<80}"
            f"{result.distances[destination]} m"
        )


def simulate_growth(
    graph
):
    """
    Simula expansão da colônia.

    A habitação recebe 30%
    de aumento de carga.
    """

    EnergyGrowth.increase_load(
        graph,
        vertex_id=7,
        percentage=30
    )


def main():
    """
    Executa a simulação completa
    da infraestrutura da colônia.
    """

    graph = (
        ColonyGraphBuilder()
        .build()
    )

    print(
        "\nTOPOLOGIA DA COLÔNIA\n"
    )

    RichGraphPrinter().print_matrix(
        graph
    )

    GraphPrinter.print_vertices(
        graph
    )

    GraphPrinter.print_edges(
        graph
    )

    print(
        "\nANÁLISE ENERGÉTICA "
        "INICIAL\n"
    )

    EnergyPrinter.print_modules(
        graph
    )

    EnergyPrinter.print_total(
        graph
    )

    print_shortest_paths(
        graph,
        CENTRO
    )

    print(
        "\nSIMULAÇÃO DE "
        "CRESCIMENTO\n"
    )

    simulate_growth(graph)

    print(
        "\nANÁLISE ENERGÉTICA "
        "APÓS EXPANSÃO\n"
    )

    EnergyPrinter.print_modules(
        graph
    )

    EnergyPrinter.print_total(
        graph
    )


if __name__ == "__main__":
    main()