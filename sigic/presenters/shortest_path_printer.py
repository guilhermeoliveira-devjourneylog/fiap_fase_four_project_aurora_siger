from rich.console import Console
from rich.table import Table

from algorithms.dijkstra import reconstruct_path


class ShortestPathPrinter:
    """
    Responsável apenas por exibir caminhos mínimos.
    """

    def __init__(self, graph):
        self.graph = graph
        self.console = Console()

    def print(self, result, source: int):
        """
        Exibe os menores caminhos a partir da origem.
        """

        table = Table(
            title="Menores Caminhos a Partir do Centro",
            show_lines=True
        )

        table.add_column(
            "Destino",
            style="cyan",
            no_wrap=True
        )

        table.add_column(
            "Caminho",
            style="green"
        )

        table.add_column(
            "Distância (m)",
            justify="right",
            style="yellow"
        )

        for destination in range(self.graph.size):

            path = reconstruct_path(
                result.previous,
                destination
            )

            names = [
                self.graph.vertices[v].name
                for v in path
            ]

            table.add_row(
                self.graph.vertices[destination].name,
                " → ".join(names),
                f"{result.distances[destination]:.0f}"
            )

        self.console.print()
        self.console.print(table)