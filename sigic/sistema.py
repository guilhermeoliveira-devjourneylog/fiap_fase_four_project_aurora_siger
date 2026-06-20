from builders.colony_graph_builder import ColonyGraphBuilder

from presenters.graph_printer import GraphPrinter
from presenters.rich_graph_printer import RichGraphPrinter
from presenters.energy_printer import EnergyPrinter

from algorithms.dijkstra import DijkstraAlgorithm

from presenters.shortest_path_printer import ShortestPathPrinter
from simulations.colony_growth_simulation import ColonyGrowthSimulation


CENTRO = 0


def main():
    """
    Executa a simulação completa da infraestrutura da colônia.
    """

    graph = ColonyGraphBuilder().build()

    print("\nTOPOLOGIA DA COLÔNIA\n")

    RichGraphPrinter().print_matrix(graph)
    GraphPrinter.print_vertices(graph)
    GraphPrinter.print_edges(graph)

    print("\nANÁLISE ENERGÉTICA INICIAL\n")

    EnergyPrinter.print_modules(graph)
    EnergyPrinter.print_total(graph)

    # ---- Simulação crescimento ----
    print("\nSIMULAÇÃO DE CRESCIMENTO\n")

    ColonyGrowthSimulation().simulate(graph)

    print("\nANÁLISE ENERGÉTICA APÓS EXPANSÃO\n")

    EnergyPrinter.print_modules(graph)
    EnergyPrinter.print_total(graph)

        # ---- Dijkstra ----
    algorithm = DijkstraAlgorithm()
    result = algorithm.execute(graph, CENTRO)

    ShortestPathPrinter(graph).print(result, CENTRO)


if __name__ == "__main__":
    main()