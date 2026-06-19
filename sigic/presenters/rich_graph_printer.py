from rich.console import Console
from rich.table import Table


class RichGraphPrinter:

    console = Console()

    def print_matrix(self, graph):

        table = Table(
            title="Matriz de Adjacência"
        )

        table.add_column("")

        for vertex in graph.vertices.values():

            table.add_column(
                vertex.name[:8]
            )

        for i in range(graph.size):

            row = [
                graph.vertices[i].name
            ]

            for value in graph.adj_matrix[i]:

                row.append(
                    str(value)
                    if value is not None
                    else "-"
                )

            table.add_row(*row)

        self.console.print(table)