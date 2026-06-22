from rich.console import Console
from rich.table import Table

console = Console()


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
        """

        table = Table(
            title="VÉRTICES",
            show_header=True,
            header_style="bold cyan"
        )

        table.add_column(
            "ID",
            justify="right",
            style="yellow"
        )

        table.add_column(
            "Nome",
            style="green"
        )

        for vertex in graph.vertices.values():

            table.add_row(
                str(vertex.id),
                vertex.name
            )

        console.print()
        console.print(table)

    @staticmethod
    def print_edges(graph):
        """
        Exibe todas as arestas do grafo e suas respectivas distâncias.
        """

        table = Table(
            title="ARESTAS",
            show_header=True,
            header_style="bold cyan"
        )

        table.add_column(
            "Origem",
            style="green"
        )

        table.add_column(
            "Destino",
            style="green"
        )

        table.add_column(
            "Distância (m)",
            justify="right",
            style="yellow"
        )

        total = 0

        for i in range(graph.size):

            for j in range(i + 1, graph.size):

                distance = graph.get_distance(
                    i,
                    j
                )

                if distance is not None:

                    table.add_row(
                        graph.vertices[i].name,
                        graph.vertices[j].name,
                        str(distance)
                    )

                    total += 1

        console.print()
        console.print(table)

        console.print(
            f"\n[bold cyan]TOTAL DE ARESTAS:[/bold cyan] "
            f"[yellow]{total}[/yellow]"
        )