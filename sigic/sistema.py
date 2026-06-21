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

from presenters.energy_distribution_printer import (
    EnergyDistributionPrinter
)

from algorithms.dijkstra import (
    DijkstraAlgorithm
)

from presenters.shortest_path_printer import (
    ShortestPathPrinter
)

from simulations.colony_growth_simulation import (
    ColonyGrowthSimulation
)

CENTRO = 0


def main():
    """
    Executa a simulação completa
    da infraestrutura da colônia.
    """

    graph = (
        ColonyGraphBuilder()
        .build()
    )

    # -------------------------
    # Topologia
    # -------------------------

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

    # -------------------------
    # Energia inicial
    # -------------------------

    print(
        "\nANÁLISE ENERGÉTICA INICIAL\n"
    )

    EnergyPrinter.print_modules(
        graph
    )

    EnergyPrinter.print_total(
        graph
    )

    EnergyDistributionPrinter.print_report(
        graph
    )

    # -------------------------
    # Crescimento
    # -------------------------

    print(
        "\nSIMULAÇÃO DE CRESCIMENTO\n"
    )

    ColonyGrowthSimulation().simulate(
        graph
    )

    # -------------------------
    # Energia após expansão
    # -------------------------

    print(
        "\nANÁLISE ENERGÉTICA APÓS EXPANSÃO\n"
    )

    EnergyPrinter.print_modules(
        graph
    )

    EnergyPrinter.print_total(
        graph
    )

    EnergyDistributionPrinter.print_report(
        graph
    )

    # -------------------------
    # Dijkstra
    # -------------------------

    print(
        "\nROTAS MÍNIMAS\n"
    )

    algorithm = (
        DijkstraAlgorithm()
    )

    result = algorithm.execute(
        graph,
        CENTRO
    )

    ShortestPathPrinter(
        graph
    ).print(
        result,
        CENTRO
    )


if __name__ == "__main__":
    main()