from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.rule import Rule

from builders.colony_graph_builder import ColonyGraphBuilder

from presenters.graph_printer import GraphPrinter
from presenters.rich_graph_printer import RichGraphPrinter
from presenters.energy_printer import EnergyPrinter
from presenters.energy_distribution_printer import (
    EnergyDistributionPrinter
)
from presenters.shortest_path_printer import (
    ShortestPathPrinter
)

from algorithms.dijkstra import (
    DijkstraAlgorithm
)

from simulations.colony_growth_simulation import (
    ColonyGrowthSimulation
)

CENTRO = 0

console = Console()


def build_graph():
    return ColonyGraphBuilder().build()


def show_topology(graph):
    console.print(
        Rule(
            "[bold cyan]TOPOLOGIA DA COLÔNIA[/bold cyan]"
        )
    )

    RichGraphPrinter().print_matrix(graph)

    GraphPrinter.print_vertices(graph)
    GraphPrinter.print_edges(graph)


def show_initial_energy(graph):
    console.print(
        Rule(
            "[bold green]ANÁLISE ENERGÉTICA INICIAL[/bold green]"
        )
    )

    EnergyPrinter.print_modules(graph)
    EnergyPrinter.print_total(graph)

    EnergyDistributionPrinter.print_report(graph)


def run_growth(graph):
    console.print(
        Rule(
            "[bold yellow]SIMULAÇÃO DE CRESCIMENTO[/bold yellow]"
        )
    )

    ColonyGrowthSimulation().simulate(graph)

    console.print(
        "[green]✓ Crescimento aplicado com sucesso.[/green]"
    )


def show_post_growth_energy(graph):
    console.print(
        Rule(
            "[bold green]ANÁLISE ENERGÉTICA APÓS EXPANSÃO[/bold green]"
        )
    )

    EnergyPrinter.print_modules(graph)
    EnergyPrinter.print_total(graph)

    EnergyDistributionPrinter.print_report(graph)


def run_dijkstra(graph):
    console.print(
        Rule(
            "[bold magenta]ROTAS MÍNIMAS[/bold magenta]"
        )
    )

    algorithm = DijkstraAlgorithm()

    result = algorithm.execute(
        graph,
        CENTRO
    )

    ShortestPathPrinter(graph).print(
        result,
        CENTRO
    )


def menu():
    console.print()

    console.print(
        Panel.fit(
            (
                "[bold cyan]SISTEMA DA COLÔNIA[/bold cyan]\n\n"
                "[1] Exibir topologia\n"
                "[2] Energia inicial\n"
                "[3] Simular crescimento\n"
                "[4] Energia após crescimento\n"
                "[5] Rotas mínimas (Dijkstra)\n"
                "[0] Sair"
            ),
            title="Menu Principal",
            border_style="blue"
        )
    )


def main():
    graph = build_graph()

    while True:

        menu()

        option = Prompt.ask(
            "[bold yellow]Escolha uma opção[/bold yellow]",
            default="0"
        )

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
                console.print(
                    "\n[bold red]Encerrando sistema...[/bold red]"
                )
                break

            case _:
                console.print(
                    "[red]Opção inválida![/red]"
                )


if __name__ == "__main__":
    main()