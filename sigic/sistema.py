from builders.colony_graph_builder import ColonyGraphBuilder

from presenters.graph_printer import GraphPrinter
from presenters.rich_graph_printer import RichGraphPrinter
from presenters.energy_printer import EnergyPrinter
from presenters.energy_distribution_printer import EnergyDistributionPrinter
from presenters.shortest_path_printer import ShortestPathPrinter

from algorithms.dijkstra import DijkstraAlgorithm
from simulations.colony_growth_simulation import ColonyGrowthSimulation

CENTRO = 0


def build_graph():
    return ColonyGraphBuilder().build()


def show_topology(graph):
    print("\nTOPOLOGIA DA COLÔNIA\n")

    RichGraphPrinter().print_matrix(graph)
    GraphPrinter.print_vertices(graph)
    GraphPrinter.print_edges(graph)


def show_initial_energy(graph):
    print("\nANÁLISE ENERGÉTICA INICIAL\n")

    EnergyPrinter.print_modules(graph)
    EnergyPrinter.print_total(graph)
    EnergyDistributionPrinter.print_report(graph)


def run_growth(graph):
    print("\nSIMULAÇÃO DE CRESCIMENTO\n")

    ColonyGrowthSimulation().simulate(graph)


def show_post_growth_energy(graph):
    print("\nANÁLISE ENERGÉTICA APÓS EXPANSÃO\n")

    EnergyPrinter.print_modules(graph)
    EnergyPrinter.print_total(graph)
    EnergyDistributionPrinter.print_report(graph)


def run_dijkstra(graph):
    print("\nROTAS MÍNIMAS\n")

    algorithm = DijkstraAlgorithm()

    result = algorithm.execute(graph, CENTRO)

    ShortestPathPrinter(graph).print(result, CENTRO)


def menu():
    print("\n==============================")
    print(" SISTEMA DA COLÔNIA - MENU")
    print("==============================")
    print("1 - Exibir topologia")
    print("2 - Energia inicial")
    print("3 - Simular crescimento")
    print("4 - Energia após crescimento")
    print("5 - Rotas mínimas (Dijkstra)")
    print("0 - Sair")
    print("==============================")


def main():
    graph = build_graph()

    while True:
        menu()
        option = input("Escolha uma opção: ")

        match option:
            case "1":
                show_topology(graph)

            case "2":
                show_initial_energy(graph)

            case "3":
                run_growth(graph)

            case "4":
                show_post_growth_energy(graph)

            case "5":
                run_dijkstra(graph)

            case "0":
                print("Encerrando sistema...")
                break

            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    main()