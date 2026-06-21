from algorithms.energy_consumption import (
    EnergyConsumption
)

from algorithms.dijkstra import (
    DijkstraAlgorithm
)


class EnergyDistribution:
    """
    Algoritmos relacionados à distribuição
    energética da colônia.
    """

    ENERGY_MODULE_ID = 5

    LOSS_FACTOR = 0.01

    @staticmethod
    def generation_capacity(
        graph
    ) -> float:
        """
        Retorna a capacidade de geração
        do módulo de energia.

        Args:
            graph (Graph): Grafo da colônia.

        Returns:
            float: Capacidade de geração.
        """

        return (
            graph
            .vertices[
                EnergyDistribution
                .ENERGY_MODULE_ID
            ]
            .generation_capacity
        )

    @staticmethod
    def total_demand(
        graph
    ) -> float:
        """
        Retorna a demanda energética total.

        Args:
            graph (Graph): Grafo da colônia.

        Returns:
            float: Demanda total.
        """

        return EnergyConsumption.total(
            graph
        )

    @staticmethod
    def coverage(
        graph
    ) -> float:
        """
        Calcula a cobertura energética.

        Valor maior que 1 indica sobra.
        Valor menor que 1 indica déficit.

        Args:
            graph (Graph): Grafo.

        Returns:
            float: Cobertura.
        """

        generation = (
            EnergyDistribution
            .generation_capacity(graph)
        )

        demand = (
            EnergyDistribution
            .total_demand(graph)
        )

        return generation / demand

    @staticmethod
    def balance(
        graph
    ) -> float:
        """
        Calcula o saldo energético.

        Args:
            graph (Graph): Grafo.

        Returns:
            float:
                Positivo = sobra.
                Negativo = déficit.
        """

        generation = (
            EnergyDistribution
            .generation_capacity(graph)
        )

        demand = (
            EnergyDistribution
            .total_demand(graph)
        )

        return generation - demand

    @staticmethod
    def transmission_losses(
        graph
    ) -> float:
        """
        Calcula perdas energéticas
        utilizando as menores rotas
        a partir do módulo de energia.

        Args:
            graph (Graph): Grafo.

        Returns:
            float: Perdas.
        """

        dijkstra = (
            DijkstraAlgorithm()
        )

        result = dijkstra.execute(
            graph,
            EnergyDistribution.ENERGY_MODULE_ID
        )

        distances = result.distances

        total_distance = 0

        for vertex_id in graph.vertices:

            if (
                vertex_id ==
                EnergyDistribution
                .ENERGY_MODULE_ID
            ):
                continue

            total_distance += (
                distances[vertex_id]
            )

        return (
            total_distance *
            EnergyDistribution
            .LOSS_FACTOR
        )

    @staticmethod
    def delivered_energy(
        graph
    ) -> float:
        """
        Energia efetivamente entregue.

        Returns:
            float
        """

        demand = (
            EnergyDistribution
            .total_demand(graph)
        )

        losses = (
            EnergyDistribution
            .transmission_losses(
                graph
            )
        )

        return max(
            demand - losses,
            0
        )

    @staticmethod
    def edei(
        graph
    ) -> float:
        """
        Energy Distribution
        Efficiency Index.

        Returns:
            float
        """

        generation = (
            EnergyDistribution
            .generation_capacity(graph)
        )

        delivered = (
            EnergyDistribution
            .delivered_energy(
                graph
            )
        )

        return delivered / generation

    @staticmethod
    def classification(
        graph
    ) -> str:
        """
        Classifica o EDEI.

        Returns:
            str
        """

        index = (
            EnergyDistribution
            .edei(graph)
        )

        if index >= 0.90:
            return "Excelente"

        if index >= 0.75:
            return "Boa"

        if index >= 0.60:
            return "Regular"

        return "Crítica"