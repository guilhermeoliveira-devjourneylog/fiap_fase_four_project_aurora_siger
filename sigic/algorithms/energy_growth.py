from models.graph import Graph


class EnergyGrowth:
    """
    Algoritmos relacionados ao crescimento
    da infraestrutura.
    """

    @staticmethod
    def increase_load(
        graph: Graph,
        vertex_id: int,
        percentage: float
    ) -> None:
        """
        Aumenta a carga de um módulo.

        Args:
            graph (Graph): Grafo da colônia.
            vertex_id (int): Módulo afetado.
            percentage (float): Percentual.
        """

        vertex = graph.vertices[vertex_id]

        vertex.current_load *= (
            1 + percentage / 100
        )

    @staticmethod
    def add_consumption(
        graph: Graph,
        vertex_id: int,
        amount: float
    ) -> None:
        """
        Incrementa consumo base.

        Args:
            graph (Graph): Grafo.
            vertex_id (int): Módulo.
            amount (float): Valor.
        """

        vertex = graph.vertices[vertex_id]

        vertex.base_consumption += amount