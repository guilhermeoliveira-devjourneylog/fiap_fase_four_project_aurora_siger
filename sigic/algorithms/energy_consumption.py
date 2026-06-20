from models.graph import Graph


class EnergyConsumption:
    """
    Algoritmos de consumo energético.
    """

    @staticmethod
    def total(
        graph: Graph
    ) -> float:
        """
        Calcula o consumo total da colônia.

        Args:
            graph (Graph): Grafo da colônia.

        Returns:
            float: Consumo total.
        """

        return sum(

            vertex.consumption

            for vertex

            in graph.vertices.values()
        )

    @staticmethod
    def by_module(
        graph: Graph
    ) -> dict[str, float]:
        """
        Retorna o consumo de cada módulo.

        Args:
            graph (Graph): Grafo da colônia.

        Returns:
            dict[str, float]:
                Consumo por módulo.
        """

        return {

            vertex.name:
            vertex.consumption

            for vertex

            in graph.vertices.values()
        }