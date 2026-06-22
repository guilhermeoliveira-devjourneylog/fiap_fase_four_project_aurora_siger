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
    """
    Controlador principal do sistema da colônia.

    Responsável por orquestrar o fluxo da aplicação, conectando:
    - Interface de menu (MenuController)
    - Construção do grafo da colônia
    - Simulações de crescimento
    - Análises energéticas
    - Algoritmos de rotas (Dijkstra)
    - Camada de apresentação (printers)

    Atua como ponto central de coordenação entre UI, algoritmos e visualização.
    """

    def __init__(self):
        """
        Inicializa o sistema.

        Cria:
        - Console Rich para saída formatada
        - Menu de interação com o usuário
        - Grafo inicial da colônia via ColonyGraphBuilder
        """
        self.console = Console()
        self.menu = MenuController()
        self.graph = ColonyGraphBuilder().build()

    def run(self):
        """
        Inicia o loop principal do sistema.

        Exibe o menu continuamente e executa as operações escolhidas pelo usuário,
        como:
        - Exibição da topologia
        - Análises energéticas
        - Simulação de crescimento
        - Cálculo de rotas mínimas
        """
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
        """
        Exibe a topologia completa da colônia.

        Mostra:
        - Matriz de adjacência (visual Rich)
        - Lista de vértices
        - Lista de arestas
        """
        self.console.print(Rule("[bold cyan]TOPOLOGIA DA COLÔNIA[/bold cyan]"))

        RichGraphPrinter().print_matrix(self.graph)
        GraphPrinter.print_vertices(self.graph)
        GraphPrinter.print_edges(self.graph)

    def show_initial_energy(self):
        """
        Exibe a análise energética inicial da colônia.

        Inclui:
        - Consumo por módulo
        - Consumo total
        - Distribuição energética
        """
        self.console.print(Rule("[bold green]ANÁLISE ENERGÉTICA INICIAL[/bold green]"))

        EnergyPrinter.print_modules(self.graph)
        EnergyPrinter.print_total(self.graph)
        EnergyDistributionPrinter.print_report(self.graph)

    def run_growth(self):
        """
        Executa a simulação de crescimento da colônia.

        Atualiza a estrutura do grafo simulando expansão da infraestrutura.
        """
        self.console.print(Rule("[bold yellow]SIMULAÇÃO DE CRESCIMENTO[/bold yellow]"))

        ColonyGrowthSimulation().simulate(self.graph)

        self.console.print("[green]✓ Crescimento aplicado com sucesso.[/green]")

    def show_post_growth_energy(self):
        """
        Exibe a análise energética após a simulação de crescimento.

        Reavalia:
        - Consumo por módulo
        - Consumo total
        - Distribuição energética atualizada
        """
        self.console.print(Rule("[bold green]ANÁLISE ENERGÉTICA APÓS EXPANSÃO[/bold green]"))

        EnergyPrinter.print_modules(self.graph)
        EnergyPrinter.print_total(self.graph)
        EnergyDistributionPrinter.print_report(self.graph)

    def run_dijkstra(self):
        """
        Executa o algoritmo de Dijkstra a partir do nó central.

        Calcula:
        - Caminhos mínimos do centro da colônia para os demais módulos
        - Exibe os resultados formatados via ShortestPathPrinter
        """
        self.console.print(Rule("[bold magenta]ROTAS MÍNIMAS[/bold magenta]"))

        algorithm = DijkstraAlgorithm()
        result = algorithm.execute(self.graph, CENTRO)

        ShortestPathPrinter(self.graph).print(result, CENTRO)