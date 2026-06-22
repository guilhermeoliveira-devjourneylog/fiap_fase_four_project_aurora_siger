from rich.console import Console
from rich.table import Table

class RichGraphPrinter:
    """
    Responsável por exibir a matriz de adjacência de um grafo
    utilizando a biblioteca Rich para uma apresentação formatada
    em tabela no terminal.

    Esta classe tem como objetivo apenas a camada de apresentação,
    sem interferir na lógica de estrutura ou algoritmos do grafo.
    """

    def __init__(self):
        """
        Inicializa o console do Rich utilizado para renderização
        das tabelas no terminal.
        """
        self.console = Console()

    def print_matrix(self, graph):
        """
        Exibe a matriz de adjacência do grafo em formato tabular.

        Cada linha representa um vértice de origem e cada coluna
        representa a conexão (ou ausência dela) com outros vértices.

        Args:
            graph: Estrutura de grafo contendo:
                - vertices: dicionário ou lista de vértices com atributo `name`
                - adj_matrix: matriz de adjacência (lista 2D)
                - size: número total de vértices

        Returns:
            None
        """

        table = Table(title="Matriz de Adjacência")

        table.add_column("")

        for vertex in graph.vertices.values():
            table.add_column(vertex.name[:8])

        for i in range(graph.size):
            row = [graph.vertices[i].name]

            for value in graph.adj_matrix[i]:
                row.append(
                    str(value) if value is not None else "-"
                )

            table.add_row(*row)

        self.console.print(table)