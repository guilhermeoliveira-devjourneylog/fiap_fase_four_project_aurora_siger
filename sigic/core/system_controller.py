from builders.colony_graph_builder import ColonyGraphBuilder

from presenters.graph_printer import GraphPrinter
from presenters.rich_graph_printer import RichGraphPrinter
from presenters.energy_printer import EnergyPrinter
from presenters.energy_distribution_printer import EnergyDistributionPrinter
from presenters.shortest_path_printer import ShortestPathPrinter

from algorithms.dijkstra import DijkstraAlgorithm
from simulations.colony_growth_simulation import ColonyGrowthSimulation

from ui.menu_controller import MenuController

from rich.console import Console
from rich.rule import Rule

CENTRO = 0


class SystemController:
    def __init__(self):
        self.console = Console()
        self.menu = MenuController()
        self.graph = ColonyGraphBuilder().build()

    def run(self):
        while True:
            self.menu.show()
            option = self.menu.get_option()

            match option:
                case "1":
                    self.show_topology()

                case "2":
                    self.show_initial_energy()

                case "3":
                    self.run_growth()

                case "4":
                    self.show_post_growth_energy()

                case "5":
                    self.run_dijkstra()

                case "0":
                    self.console.print("\n[bold red]Encerrando sistema...[/bold red]")
                    break

                case _:
                    self.console.print("[red]Opção inválida![/red]")

    # ------------------ CASOS DE USO ------------------

    def show_topology(self):
        self.console.print(Rule("[bold cyan]TOPOLOGIA DA COLÔNIA[/bold cyan]"))

        RichGraphPrinter().print_matrix(self.graph)
        GraphPrinter.print_vertices(self.graph)
        GraphPrinter.print_edges(self.graph)

    def show_initial_energy(self):
        self.console.print(Rule("[bold green]ANÁLISE ENERGÉTICA INICIAL[/bold green]"))

        EnergyPrinter.print_modules(self.graph)
        EnergyPrinter.print_total(self.graph)
        EnergyDistributionPrinter.print_report(self.graph)

    def run_growth(self):
        self.console.print(Rule("[bold yellow]SIMULAÇÃO DE CRESCIMENTO[/bold yellow]"))

        ColonyGrowthSimulation().simulate(self.graph)

        self.console.print("[green]✓ Crescimento aplicado com sucesso.[/green]")

    def show_post_growth_energy(self):
        self.console.print(Rule("[bold green]ANÁLISE ENERGÉTICA APÓS EXPANSÃO[/bold green]"))

        EnergyPrinter.print_modules(self.graph)
        EnergyPrinter.print_total(self.graph)
        EnergyDistributionPrinter.print_report(self.graph)

    def run_dijkstra(self):
        self.console.print(Rule("[bold magenta]ROTAS MÍNIMAS[/bold magenta]"))

        algorithm = DijkstraAlgorithm()
        result = algorithm.execute(self.graph, CENTRO)

        ShortestPathPrinter(self.graph).print(result, CENTRO)